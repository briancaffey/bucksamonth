from django.conf.urls import url, include
from . import views

urlpatterns = [

	url(r'^$', views.all_categories, name='all_categories'),
    url(r'^(?P<slug>.+)/$', views.category_view, name='category_view'),

]
