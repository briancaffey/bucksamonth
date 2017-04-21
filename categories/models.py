from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)
    emoji = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.category)

    # def cat_count(self):
    #     count = Service.objects.filter(category=self.category)
    #     return len(count)

def create_slug(instance):
    slug = slugify(instance.category)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Category)
