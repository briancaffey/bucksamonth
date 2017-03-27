from django import forms
from django.forms import Select
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from services.models import Subscription, Service


class MyAuthenticationForm(AuthenticationForm):

	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "enter your username",
		}))

	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': "enter your password",}))


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(
		required=True, 
		widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "your email",
		}))

	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "pick a username for your public profile",
		}))

	first_name = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "your name (optional)",
		}))

	last_name = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "your last name (optional)",
		}))

	password1 = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class':'form-control', 
		'placeholder': "choose a password",
		}))

	password2 = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class':'form-control', 
		'placeholder': "type it again",
		}))


	class Meta:
		model = User
		fields = (
			'email', 
			'username',
			'first_name',
			'last_name', 
			'password1', 
			'password2', 
			)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit: 
			user.save()

		return user

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
				'email', 
				'first_name',
				'last_name',
				'password',
				)


class AddSubscriptionForm(forms.ModelForm):

	service = forms.ModelChoiceField(
		queryset=Service.objects.order_by('service_name').extra(select={'lower_name':'lower(service_name)'}).order_by('lower_name'), 
		widget=forms.Select(attrs={
			'class':'form-control',
			'placeholder':'select a subscrption service',
			})
		)

	cc_nickname = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "which credit card is it on (nickname)",
		}))

	bucksamonth = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "how many bucks a month?",
		}))

	class Meta:
		model = Subscription
		fields = (

				'service', 
				'cc_nickname', 
				'bucksamonth',

				)
