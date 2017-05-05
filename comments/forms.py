from django import forms
from .models import Comment

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    emoji = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder': "emoji comment",
        }))

    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
            'class':'form-control',
            'rows':'2',
            'placeholder': "write your comment here",
        }))


    class Meta:
        model = Comment
        fields = [
            'emoji',
            'content',
        ]
