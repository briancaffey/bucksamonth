from django import forms

# from pagedown.widgets import PagedownWidget
from taggit.forms import TagWidget
from .models import Post
import datetime

YEAR_CHOICES = tuple([2000+i for i in range(22)])

class PostForm(forms.ModelForm):


    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder': "title goes here",}
    ))

    emoji = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder': "emoji go here",}
    ))



    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
            'class':'form-control',
            'placeholder': "write your post here",}
    ))

    draft = forms.BooleanField(
        initial=False,
		required=False,
		widget=forms.CheckboxInput(

		attrs={
		})
    )
	# content = forms.CharField(widget=PagedownWidget(show_preview=False))

    # content = forms.CharField(widget=forms.Textarea)
    # publish = forms.DateField(widget=forms.SelectDateWidget)
    publish = forms.DateField(
        initial = datetime.date.today,
        widget=forms.SelectDateWidget(

        years=YEAR_CHOICES)
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'emoji',
            'content',
            'draft',
            'publish',
            'tags'
        ]
        widgets = {
            'tags': TagWidget(attrs={
                'class':'form-control',
            })
        }
