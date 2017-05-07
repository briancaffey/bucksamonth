from django.conf.urls import url
from . import views
from user_messages.views import (
	inbox,
	new_message,
	messages,
)
from accounts.views import AddSubscriptionView, UpdateUserInfoForm
from accounts.forms import MyAuthenticationForm
from users.views import SubscriptionUpdate, SubscriptionDeleteView
from django.contrib.auth.views import (
	login, logout, password_reset, password_reset_done, password_reset_confirm,
	password_reset_complete,
)

urlpatterns = [


	url(r'^messages/conversation/(?P<username>.+)/', messages, name="messages" ),
	url(r'^messages/new/$', new_message, name='new_message'),
	url(r'^messages/$', inbox, name='inbox'),

	url(r'^setup/$', views.setup, name='setup'),
	url(r'^please-confirm-email/$', views.confirm_email, name='confirm_email'),
	url(r'^confirm-email/(?P<uid>.+)/$', views.email_confirmed, name="email_confirmed"),
	url(r'^profile/edit/$', views.update_personal_info, name='update_personal_info'),
	#url(r'^(?P<pk>[0-9]+)/info/$', UpdateUserInfoForm.as_view(), name='update_personal_info'),
	url(r'^add-subscription/$', AddSubscriptionView.as_view(), name='add_subscription'),
	url(r'^subscription/(?P<pk>[0-9]+)/edit/$', SubscriptionUpdate.as_view(), name='subscription_update'),
	url(r'^subscription/(?P<pk>[0-9]+)/delete/$', views.delete_subscription, name="delete_subscription"),
	url(r'^login/$', views.login_view, name="login"),

	#url(r'^login/$', login, {'template_name': 'accounts/login.html', 'authentication_form': MyAuthenticationForm}, name="login"),
	url(r'^logout/$', views.logout_view, name="logout"),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.view_profile, name='profile'),
	url(r'^edit/$', views.edit_profile, name='edit'),
	url(r'^profile/password/$', views.change_password, name='change_password'),
	url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect':'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'},name='reset_password'),
	url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect':'accounts:password_reset_complete'}, name='password_reset_confirm'),
	url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),

]
