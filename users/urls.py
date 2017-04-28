from django.conf.urls import url, include
from users.views import view_profile
from friends.views import add_or_remove_friends

urlpatterns = [

    url(r'^(?P<username>.+)/(?P<verb>.+)/$', add_or_remove_friends, name="add_or_remove_friends"),
	url(r'^(?P<username>.+)/$', view_profile, name='view_profile'),




]
