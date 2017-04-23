from django.db import models
from accounts.models import UserProfile
from django.contrib.auth.models import User
from datetime import date
from categories.models import Category
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType

# Create your models here.
# Create your models here.
class Service(models.Model):
	service_name 			= models.CharField(max_length=140)
	url_name 				= models.CharField(max_length=200)
	description_long		= models.CharField(max_length=500, default='')
	description_short		= models.CharField(max_length=140, default='')
	category				= models.ManyToManyField(Category, blank=True)
	featured				= models.BooleanField(default=False)
	date_created 			= models.DateField(auto_now=True)
	bucksamonth 			= models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	emoji					= models.CharField(max_length=20, default='')
	twitter 				= models.CharField(max_length=100, default='')

	def __str__(self):
		return str(self.service_name)

	def comments(self):
		return Comment.objects.filter(service=self.id)

	def get_absolute_url(self):
		return "/services/%i/" % self.id

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

# class Comment(models.Model):
# 	service 				= models.ForeignKey(Service, on_delete=models.CASCADE)
# 	user 					= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_commenter")
# 	text 					= models.CharField(max_length=1000)
# 	date_created			= models.DateField(auto_now_add=True)
# 	votes 					= models.IntegerField(default=0)
# 	emoji 					= models.CharField(max_length=20, default='')
#
# 	class Meta:
# 		ordering = ['-date_created']
#
# 	def __str__(self):
# 		return str(self.emoji)

class Subscription(models.Model):
	service 				= models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subscription_service')
	user 					= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="subscribed_user")
	cc_nickname 			= models.CharField(max_length=10)
	bucksamonth 			= models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	date_created			= models.DateField(default=date.today)
	wishlist				= models.BooleanField(default=False)
	private					= models.BooleanField(default=False)

	def __str__(self):
		return str(self.service)
