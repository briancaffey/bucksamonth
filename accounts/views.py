from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import UserProfile
from services.models import Subscription, Comment

from django.conf import settings
from django.core.mail import send_mail
EMAIL_HOST_USER = settings.EMAIL_HOST_USER

from django.views.decorators.csrf import csrf_protect

from accounts.forms import (
	RegistrationForm,
	EditProfileForm,
	EditPersonalInfoForm,
	AddSubscriptionForm,
	MyAuthenticationForm,
	UserLoginForm,
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.views.generic import View, TemplateView, FormView, UpdateView
from django.views.generic.edit import UpdateView

from django.contrib import messages


def faq(request):
	print(request.get_host())
	return render(request, 'faq.html', {})

class developers(TemplateView):
	template_name = 'developers.html'

class business(TemplateView):
	template_name = 'business.html'


def confirm_email(request):
	return render(request, 'accounts/confirm_email.html', {})

def home(request):
	return render(request, 'accounts/account_home.html')

def setup(request):

	if not request.user.userprofile.email_valid:
		return redirect('accounts:confirm_email')
	instance = UserProfile.objects.get(user=request.user)
	form = EditPersonalInfoForm(request.POST or None, instance=instance)
	context = {
		'form':form,
	}

	if request.user.is_authenticated() and request.user.userprofile.setup == False:

		if form.is_valid():
			print("OK")
			instance = form.save(commit=False)
			instance.setup = True
			instance.save()
			return redirect('accounts:profile')
		return render(request, 'accounts/userprofile_setup_form.html', context)
	else:
		return redirect('home')




@csrf_protect
def register(request):

	if request.user.is_authenticated():
		redirect('accounts:profile')

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1'],)
			login(request, new_user)
			email_ = form.cleaned_data.get('email')
			print(new_user.userprofile.uid)
			base_link = request.get_host()
			print(base_link)
			link = new_user.userprofile.get_confirm_link()
			print(link)
			confirm_link = base_link + link
			print(confirm_link)


			send_mail(		'Thanks for signing up for my bucksamonth!',
							'Hi, thanks.',
							EMAIL_HOST_USER,
							[email_],
							html_message=	"Hi, you (or possibly someone else) signed up for bucksamonth with " + new_user.email + "\
											<br /><br />Please click this link if you wish to join my newsletter:<br />\
											" + str(confirm_link) + "<br /><br />\
											If you don't want to join my newsletter please ignore this email.<br />"
											)
			return redirect('accounts:confirm_email')

		else:
			#if form.cleaned_data['password1'] != form.cleaned_data['password2']:
			#	not_unique = "confirmation password doesn't match"
			return render(request, 'accounts/reg_form.html', {'form':form})

	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def login_view(request):

	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	print(request.GET)
	print(next)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, 'Welcome back, ' + str(request.user) + '!')
		print(next)
		if next:
			print(next)
			return redirect(next.next)
		return redirect('accounts:profile')

	return render(request, 'accounts/login.html', {'form':form})

@login_required
def email_confirmed(request, uid):
	user_ = get_object_or_404(UserProfile, uid=uid)
	user_.email_valid = True
	user_.save()
	messages.success(request, "thanks for confirming your email address")
	return redirect('accounts:setup')


# def login_(request):
#
# 	form = UserLoginForm(request.POST or None)
# 	print("testing1")
# 	print(form.is_valid())
# 	if request.method == "POST":
# 		form = MyAuthenticationForm(request.POST)
# 		if form.is_valid():
# 			login_form = form.save(commit = False)
# 			print(login_form)
#
# 			logged_in_user = authenticate(username=form.cleaned_data.get('username'),
# 									password=form.cleaned_data.get('password'))
# 			login(request, logged_in_user)
# 			return redirect('accounts:profile')
# 	context = {
# 			'form': form,
# 	}
# 	return render(request, 'accounts/login.html', context)

def view_profile(request):
	if request.user.userprofile.setup == True:
		print("here")
		subscriptions = Subscription.objects.filter(user=request.user.userprofile, wishlist=False)
		bucksamonth = Subscription.objects.filter(user=request.user.userprofile)
		wishlist = Subscription.objects.filter(user=request.user.userprofile, wishlist=True)
		bucksamonth = sum([subscription.bucksamonth for subscription in subscriptions])
		comments = Comment.objects.filter(user=request.user)

		args = {'user':request.user, 'subscriptions':subscriptions, 'bucksamonth':bucksamonth, 'wishlist':wishlist, 'comments':comments}
		#args = {'user': request.user, 'subscriptions':subscriptions, 'bucksamonth':bucksamonth}
		return render(request, 'accounts/profile.html', args)

	return redirect('accounts:setup')

class AddSubscriptionView(TemplateView):
	template_name = 'accounts/add_subscription.html'

	def get(self, request):
		form = AddSubscriptionForm()
		args = {'form': form}
		return render(request, self.template_name, args)

	def post(self, request):
		form = AddSubscriptionForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user.userprofile
			post.save()

			return redirect('accounts:profile')
		else:
			return render(request, self.template_name, {"form": form})


def update_personal_info(request):
	if request.user.is_authenticated():
		user_profile = UserProfile.objects.get(user=request.user)
		form = EditPersonalInfoForm(request.POST or None, instance=request.user.userprofile)
		context = {
			'form':form,
		}

		if request.method=="POST":
			if form.is_valid():
				instance = form.save(commit=False)
				instance.setup = True
				instance.save()
				return redirect('accounts:profile')

		return render(request, 'accounts/userprofile_form.html', context)

	else:
		messages.success(request, "you can't do that")
		return redirect('services:home')

class UpdateUserInfoForm(UpdateView):

	model = UserProfile
	form_class = EditPersonalInfoForm
	#fields = ['description']
	success_url = '/account/profile/'

	def get_context_data(self, **kwargs):
		context = super(UpdateUserInfoForm, self).get_context_data(**kwargs)
		context['subscription'] = self.object
		return context



def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile/')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form':form}
		return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile/')
		else:
			return redirect('/account/change-password/')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form':form}
		return render(request, 'accounts/change_password.html', args)
