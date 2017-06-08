from rest_framework.serializers import ModelSerializer

from rest_framework import serializers

from services.models import Subscription


class SubscriptionListSerializer(ModelSerializer):
    service_name = serializers.ReadOnlyField()
    emoji = serializers.ReadOnlyField()
    class Meta:
        model = Subscription
        fields = [
            # 'id',
            'bucksamonth',
            # 'user',
            'date_created',
            # 'wishlist',
            # 'private',
            'emoji',
            'service_name',
        ]
