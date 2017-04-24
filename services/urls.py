from django.conf.urls import url, include
from . import views
from services.views import AddServiceView, ServiceDetailView, ServiceSubscriberListView

urlpatterns = [

	url(r'^add-new/$', views.add_service_view, name='add_service'),
	url(r'^(?P<service_slug>.+)/add/$', views.add_service_from_detail_view, name='add_service_from_detail_view'),
	url(r'^(?P<service_slug>.+)/subscribers/$', views.service_subscribers, name='service_subscribers'),
	url(r'^(?P<service_slug>.+)/$', views.service_detail, name='service_detail'),
	url(r'^$', views.services, name='services'),


	#url(r'^(?P<service_slug>.+)/subscribers/$', ServiceSubscriberListView.as_view(), name='service_subscribers'),
	#url(r'^comment/(?P<pk>[0-9]+)/delete/$', CommentDeleteView.as_view(), name='comment_delete'),

]
