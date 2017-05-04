from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^(?P<pk>.+)/delete/$', views.delete_comment, name='delete_comment'),
	url(r'^(?P<pk>.+)/flag/$', views.flag_comment, name='flag_comment'),

]
