from django.conf.urls import url, include
from users.views import view_profile

urlpatterns = [

	url(r'^(?P<pk>[0-9]+)/$', view_profile, name='view_profile'),



]
