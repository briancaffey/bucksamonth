from django.contrib import admin

from .models import Service, Comment, Subscription

# Register your models here.
admin.site.register(Service)
admin.site.register(Comment)
admin.site.register(Subscription)