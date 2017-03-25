from django.conf.urls import url, include
from users.views import UserProfileView

urlpatterns = [

	url(r'^(?P<pk>[0-9]+)/$', UserProfileView.as_view(), name='view_profile'),



]