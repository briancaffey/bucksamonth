from django.db import models
from django.contrib.auth.models import User
# django.db.models.get_model('app.Model')
# from services.models import Subscription
# from django.apps import get_model

from django.db.models import Sum

from django.db.models.signals import post_save
import uuid

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100, default='')
	twitter = models.CharField(max_length=100, default='')
	emoji = models.CharField(max_length=10, default='')
	facebook_url = models.URLField(max_length=400, blank=True)
	linkedin_url = models.URLField(max_length=400, blank=True)
	website = models.URLField(max_length=400, blank=True)
	setup = models.BooleanField(default=False)
	uid = models.CharField(default=uuid.uuid4, max_length=40)
	email_valid = models.BooleanField(default=False)
	followers = models.ManyToManyField('self')
	join_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return "/users/%s/" % self.user.username

	def get_confirm_link(self):
		return "/account/confirm-email/%s" % self.uid


	def tally_bucksamonth(self):

		from services.models import Subscription
		# sub = get_model('services.Subscription')
		bucksamonth = Subscription.objects.filter(user=self.user.userprofile).aggregate(Sum('bucksamonth'))
		if bucksamonth['bucksamonth__sum']:
			return bucksamonth['bucksamonth__sum']
		else:
			return 0.00


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
