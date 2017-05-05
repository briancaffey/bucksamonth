from django import forms
from services.models import Service

from taggit.forms import TagWidget
from .models import Post
import datetime
from django.forms.widgets import CheckboxSelectMultiple


YEAR_CHOICES = tuple([2000+i for i in range(22)])
SERVICE_CHOICES = Service.objects.order_by('service_name').extra(select={'lower_name':'lower(service_name)'}).order_by('lower_name')



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

    publish = forms.DateField(
        initial = datetime.date.today,
        widget=forms.SelectDateWidget(

        years=YEAR_CHOICES)
    )


    services = forms.widgets.CheckboxSelectMultiple(

        choices=SERVICE_CHOICES,
        )

    class Meta:
        model = Post
        fields = [
            'title',
            'emoji',
            'content',
            'draft',
            'publish',
            'tags',
            'services',
        ]
        widgets = {
            'tags': TagWidget(attrs={
                'class':'form-control',
            })
        }
