from django.conf.urls import url, include
from . import views
from services.views import AddServiceView, ServiceDetailView

urlpatterns = [

	url(r'^$', views.services, name='services'),
	url(r'^add/$', AddServiceView.as_view(), name='add_service'),
	url(r'^view/(?P<pk>[0-9])/$', ServiceDetailView.as_view(), name='service')

]