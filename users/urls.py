from django.conf.urls import url, include
from users.views import view_profile
from friends.views import add_or_remove_friends
from users.views import message_user_from_profile

urlpatterns = [
    url(r'^(?P<username>.+)/message/$', message_user_from_profile, name='message_user_from_profile'),

    url(r'^(?P<username>.+)/(?P<verb>.+)/$', add_or_remove_friends, name="add_or_remove_friends"),
	url(r'^(?P<username>.+)/$', view_profile, name='view_profile'),




]
