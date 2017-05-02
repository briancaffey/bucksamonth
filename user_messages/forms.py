from django import forms
from .models import UserMessage
from friends.models import Friend
from django.contrib.auth import get_user_model
User = get_user_model()


class MessageForm(forms.ModelForm):

    message = forms.CharField(
		label='',
		widget=forms.Textarea(
			attrs={
			'class':'form-control',
			'placeholder': "enter your message",
            'cols':4,
            }))

    class Meta:
        model = UserMessage
        fields = [
            'user',
            'message',
        ]

        widgets = {'user': forms.Select(attrs={'class':'form-control'})}
        labels = {'user':'send a message to someone you follow on bucksamonth'}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MessageForm, self).__init__(*args, **kwargs)
        friend_object = Friend.objects.get(current_user=user.userprofile)
        choices = friend_object.users.all()
        self.fields['user'].queryset = User.objects.filter(userprofile__in=choices)


class ToUserMessageForm(forms.ModelForm):
    message = forms.CharField(
		label='',
		widget=forms.Textarea(
			attrs={
			'class':'form-control',
			'placeholder': "enter your message",
            'rows':3,
            }))

    class Meta:
        model = UserMessage
        fields = [
            'message',
        ]
