from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
# from markdown_deux import markdown
# from django.utils.safestring import mark_safe
from comments.models import Comment
from services.models import Service
from django.contrib.contenttypes.models import ContentType


from taggit.managers import TaggableManager

# Create your models here.

# from .utils import get_read_time

# class PostManager(models.Manager):
#
# 	def active(self, *args, **kwargs):
# 		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

# def upload_location(instance, filename):
# 	return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    user               = models.ForeignKey(settings.AUTH_USER_MODEL)
    approved           = models.BooleanField(default=False, blank=True)
    title              = models.CharField(max_length=100)
    emoji              = models.CharField(max_length=50, blank=True)
    slug               = models.SlugField(unique=True)
    views              = models.PositiveIntegerField(default=0)
    services           = models.ManyToManyField(Service, blank=True, related_name="post_service")
    tags               = TaggableManager()
    likes              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    content            = models.TextField()
    draft              = models.BooleanField(default=False)
    publish            = models.DateField(auto_now=False, auto_now_add=False)
    updated            = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp          = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-timestamp', '-updated']

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug":self.slug})

    def get_api_like_url(self):
        return reverse("api-posts:like-api-toggle", kwargs={"slug":self.slug})

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" % (slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
