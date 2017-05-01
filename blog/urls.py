from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^a/(?P<username>.+)/', views.author_view, name='author_view'),
	url(r'^tags/$', views.all_tags, name='all_tags'),
	url(r'^tags/(?P<slug>.+)/$', views.tag_view, name='tag_view'),
	url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<slug>.+)/update/$', views.update, name='update'),
    url(r'^(?P<slug>.+)/delete/$', views.delete, name='delete'),
	url(r'^(?P<slug>.+)/$', views.detail, name='detail'),




]
