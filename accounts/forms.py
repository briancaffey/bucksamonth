from django import forms
from django.forms import Select
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from services.models import Subscription, Service
from accounts.models import UserProfile

import datetime

class MyAuthenticationForm(AuthenticationForm):

	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "enter your username",
		}))

	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'placeholder': "enter your password",}))


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
			'username',
			'email', 
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



class EditPersonalInfoForm(forms.ModelForm):

	description = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "say something about yourself...",
		}))

	twitter = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "your twitter handle",
		}))

	emoji = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "choose your emojis",
		}))




	class Meta:
		model = UserProfile
		fields = (

			'description',
			'twitter', 
			'emoji', 

			)






class EditProfileForm(UserChangeForm):

	username = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "pick a username for your public profile",
		}))

	email = forms.EmailField(
		required=True, 
		widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "update your email address",
		}))

	first_name = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "change your first name",
		}))

	last_name = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control', 
		'placeholder': "update your last name",
		}))


	class Meta:
		model = User
		fields = (
				'username',
				'email', 
				'first_name',
				'last_name',
				'password', 
				)

YEAR_CHOICES = tuple([2000+i for i in range(18)])


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


	private = forms.BooleanField(
		initial=False, 
		required=False, 
		widget=forms.CheckboxInput(

		attrs={
		
		}))



	wishlist = forms.BooleanField(
		initial=False, 
		required=False, 
		widget=forms.CheckboxInput(

		attrs={
		
		}))

	date_created = forms.DateField(
		initial=datetime.date.today,

		widget=forms.SelectDateWidget(
		
		years=YEAR_CHOICES))

	class Meta:
		model = Subscription
		fields = (

				'service', 
				'cc_nickname', 
				'bucksamonth',
				'private', 
				'wishlist', 
				'date_created'
				)

class UpdateSubscriptionForm(forms.ModelForm):

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

	date_created = forms.DateField(

		widget=forms.SelectDateWidget(
		attrs={
		},
		years=YEAR_CHOICES))

	private = forms.BooleanField(
		initial=False, 
		required=False, 
		widget=forms.CheckboxInput(

		attrs={
		
		}))



	wishlist = forms.BooleanField(
		required=False, 
		widget=forms.CheckboxInput(
		attrs={
		}))

	class Meta:
		model = Subscription
		fields = (

				'cc_nickname', 
				'bucksamonth',
				'private',
				'wishlist', 
				'date_created', 
				)

