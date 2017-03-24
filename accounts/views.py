from django.shortcuts import render, redirect
from accounts.forms import (
	RegistrationForm, 
	EditProfileForm, 
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from services.models import Subscription
from django.views.generic import View, TemplateView
from accounts.forms import AddSubscriptionForm

def home(request): 
	return render(request, 'accounts/account_home.html')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')

	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
	subscriptions = Subscription.objects.filter(user=request.user.userprofile)
	bucksamonth = Subscription.objects.filter(user=request.user.userprofile)
	bucksamonth = sum([subscription.bucksamonth for subscription in subscriptions])
	args = {'user': request.user, 'subscriptions':subscriptions, 'bucksamonth':bucksamonth}

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


def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile')

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
			return redirect('/account/profile')
		else:
			return redirect('/account/change-password')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form':form}
		return render(request, 'accounts/change_password.html', args)