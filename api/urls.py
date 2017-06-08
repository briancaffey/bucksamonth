from django.conf.urls import url
from .views import (
    SubscriptionListAPIView
)


urlpatterns = [

    url('^subscriptions/(?P<username>.+)/$', SubscriptionListAPIView.as_view()),

]
