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





    # emoji = forms.CharField()
    # content = forms.CharField(label='', widget=forms.Textarea(
    #     attrs={'rows':3, 'id':'post-text'}))


    class Meta:
        model = Comment
        fields = [
            'emoji',
            'content',
        ]

#
# class AddCommentForm(forms.ModelForm):
#
#
# 	text = forms.CharField(widget=forms.Textarea(
# 		attrs={
# 		'class':'form-control',
# 		'rows':'2',
# 		'placeholder': "tell us about the service",
# 		}))
#
# 	emoji = forms.CharField(widget=forms.TextInput(
# 		attrs={
# 		'class':'form-control',
# 		'placeholder': "emoji comment",
# 		}))
#
# 	class Meta:
# 		model = Comment
# 		fields = (
# 			'emoji',
# 			'text',
#
# 		)
