from django.db import models
from django.db.models import Sum
from django.db.models.signals import pre_save

from accounts.models import UserProfile
from categories.models import Category
from comments.models import Comment

from datetime import date

from django.contrib.contenttypes.models import ContentType

from django.utils.text import slugify

from taggit.managers import TaggableManager

# Create your models here.
class Service(models.Model):
	service_name 			= models.CharField(max_length=140)
	service_slug			= models.SlugField(blank=True)
	url_name 				= models.CharField(max_length=200)
	description_long		= models.CharField(max_length=500, default='')
	description_short		= models.CharField(max_length=140, default='')
	category				= models.ManyToManyField(Category, blank=True)
	featured				= models.BooleanField(default=False)
	date_created 			= models.DateField(auto_now=True)
	bucksamonth 			= models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	emoji					= models.CharField(max_length=20, default='')
	twitter 				= models.CharField(max_length=100, default='')
	tags 					= TaggableManager()

	def __str__(self):
		return str(self.service_name)

	def comments(self):
		return Comment.objects.filter(service=self.id)

	def get_absolute_url(self):
		return "/services/%s/" % self.service_slug

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

	@property
	def comments(self):
		instance = self
		qs = Comment.objects.filter_by_instance(instance)
		return qs


def create_slug(instance, new_slug=None):
	slug = slugify(instance.service_name)
	if new_slug is not None:
		slug = new_slug
	qs = Service.objects.filter(service_slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" % (slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.service_slug:
		instance.service_slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Service)

class Subscription(models.Model):
	service 				= models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subscription_service')
	user 					= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="subscribed_user")
	cc_nickname 			= models.CharField(max_length=10, default='')
	bucksamonth 			= models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	date_created			= models.DateField(default=date.today)
	wishlist				= models.BooleanField(default=False)
	private					= models.BooleanField(default=False)


	def emoji(self):
		return str(self.service.emoji)

	def service_name(self):
		return str(self.service.service_name)

	def service_link(self):
		return 'http://www.bucksamonth.com' + str(self.service.get_absolute_url())

	def service_description(self):
		return str(self.service.description_short)

	def __str__(self):
		return str(self.service)
