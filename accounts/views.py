from django.shortcuts import render, redirect

from accounts.models import UserProfile
from services.models import Subscription, Comment


from accounts.forms import (
	RegistrationForm,
	EditProfileForm,
	EditPersonalInfoForm,
	AddSubscriptionForm,
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.views.generic import View, TemplateView, FormView, UpdateView
from django.views.generic.edit import UpdateView

from django.contrib import messages

class faq(TemplateView):
	template_name = 'faq.html'

class developers(TemplateView):
	template_name = 'developers.html'

class business(TemplateView):
	template_name = 'business.html'


def home(request):
	return render(request, 'accounts/account_home.html')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1'],)
			login(request, new_user)
			return redirect('accounts:profile')

		else:
			#if form.cleaned_data['password1'] != form.cleaned_data['password2']:
			#	not_unique = "confirmation password doesn't match"
			return render(request, 'accounts/reg_form.html', {'form':form})

	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
	subscriptions = Subscription.objects.filter(user=request.user.userprofile, wishlist=False)
	bucksamonth = Subscription.objects.filter(user=request.user.userprofile)
	wishlist = Subscription.objects.filter(user=request.user.userprofile, wishlist=True)
	bucksamonth = sum([subscription.bucksamonth for subscription in subscriptions])
	comments = Comment.objects.filter(user=request.user)
	
	args = {'user':request.user, 'subscriptions':subscriptions, 'bucksamonth':bucksamonth, 'wishlist':wishlist, 'comments':comments}
	#args = {'user': request.user, 'subscriptions':subscriptions, 'bucksamonth':bucksamonth}

	return render(request, 'accounts/profile.html', args)


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
