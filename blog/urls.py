from django.conf.urls import url, include
from . import views

urlpatterns = [

	url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<slug>.+)/update/$', views.update, name='update'),
    url(r'^(?P<slug>.+)/delete/$', views.delete, name='delete'),
	url(r'^(?P<slug>.+)/$', views.detail, name='detail'),

]
