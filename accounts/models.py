from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100, default='')
	twitter = models.CharField(max_length=100, default='')
	emoji = models.CharField(max_length=10, default='')
	setup = models.BooleanField(default=False)
	uid = models.CharField(default=uuid.uuid4, max_length=40)
	email_valid = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return "/users/%s/" % self.user.username

	def get_confirm_link(self):
		return "/account/confirm-email/%s" % self.uid


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
