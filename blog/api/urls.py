from django.conf.urls import url

from .views import (

    PostLikeAPIToggle,

)

urlpatterns = [

	url(r'^(?P<slug>.+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),

]
