from django.conf.urls import url, include
from . import views
from services.views import AddServiceView, ServiceDetailView, ServiceSubscriberListView, CommentDeleteView

urlpatterns = [

	url(r'^$', views.services, name='services'),
	url(r'^add/$', AddServiceView.as_view(), name='add_service'),
	url(r'^(?P<pk>[0-9]+)/$', ServiceDetailView.as_view(), name='service_detail'),
	url(r'^view/(?P<pk>[0-9]+)/subscribers/$', ServiceSubscriberListView.as_view(), name='service_subscribers'),
	url(r'^comment/(?P<pk>[0-9]+)/delete/$', CommentDeleteView.as_view(), name='comment_delete'),

]