from django.conf.urls import url
from . import views
from accounts.views import AddSubscriptionView
from accounts.forms import MyAuthenticationForm
from users.views import SubscriptionUpdate, SubscriptionDeleteView
from django.contrib.auth.views import (
	login, logout, password_reset, password_reset_done, password_reset_confirm,
	password_reset_complete, 
)

urlpatterns = [

	url(r'^$', views.home), 
	url(r'^add-subscription/$', AddSubscriptionView.as_view(), name='add_subscription'),
	url(r'^subscription/(?P<pk>[0-9]+)/edit/$', SubscriptionUpdate.as_view(), name='subscription_update'),
	url(r'^subscription/(?P<pk>[0-9]+)/delete/$', SubscriptionDeleteView.as_view(), name="delete_subscription"),
	url(r'^login/$', login, {'template_name': 'accounts/login.html', 'authentication_form': MyAuthenticationForm}, name="login"),
	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name="logout"),
	url(r'^register/$', views.register, name='register'), 
	url(r'^profile/$', views.view_profile, name='profile'), 
	url(r'^profile/edit/$', views.edit_profile, name='edit'), 
	url(r'^profile/password/$', views.change_password, name='change_password'), 
	url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect':'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'},name='reset_password'),
	url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'), 
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect':'accounts:password_reset_complete'}, name='password_reset_confirm'), 
	url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'), 
	
]