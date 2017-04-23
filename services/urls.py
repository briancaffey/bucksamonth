from django.conf.urls import url, include
from . import views
from services.views import AddServiceView, ServiceDetailView, ServiceSubscriberListView

urlpatterns = [

	url(r'^$', views.services, name='services'),
	url(r'^add/$', AddServiceView.as_view(), name='add_service'),
	url(r'^(?P<pk>[0-9]+)/$', views.service_detail, name='service_detail'),
	url(r'^(?P<pk>[0-9]+)/add/$', views.add_service_from_detail_view, name='add_service_from_detail_view'),
	url(r'^view/(?P<pk>[0-9]+)/subscribers/$', ServiceSubscriberListView.as_view(), name='service_subscribers'),
	#url(r'^comment/(?P<pk>[0-9]+)/delete/$', CommentDeleteView.as_view(), name='comment_delete'),

]
