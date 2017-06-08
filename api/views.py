from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
from services.models import Subscription
from rest_framework.generics import (
    ListAPIView,
)

from .serializers import (
    SubscriptionListSerializer
)


class SubscriptionListAPIView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionListSerializer


    def get_queryset(self):
        """
        This view should return a list of all the subscriptions for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']

        person = get_object_or_404(User, username=username)
        person = person.userprofile
        all_subscriptions = Subscription.objects.filter(user=person, private=False)


        return all_subscriptions
