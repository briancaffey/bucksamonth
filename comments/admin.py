from django.contrib import admin

# Register your models here.

from .models import Comment


class CommentModelAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'emoji', 'content', 'content_type', 'object_id', 'flag']
    list_filter = ['content_type']
    class Meta:
        model = Comment


admin.site.register(Comment, CommentModelAdmin)
