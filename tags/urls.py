from django.conf.urls import url, include
from . import views

urlpatterns = [

	url(r'^$', views.all_tags, name='all_tags'),

	url(r'^service/(?P<tag_name>.+)/$', views.service_tag_view, name='service_tag_view'),

	url(r'^blog/(?P<tag_name>.+)/$', views.blog_tag_view, name='blog_tag_view'),

]
