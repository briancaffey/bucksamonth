from django.shortcuts import render, redirect
from .models import Comment
from django.contrib import messages

# Create your views here

def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, 'your comment was deleted')
        return redirect(comment.content_object.get_absolute_url())
    else:
        messages.success(request, 'you don\'t have permission to delete this comment')
        return redirect(comment.content_object.get_absolute_url())


def flag_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.flag += 1
    comment.save()
    messages.success(request, 'thank you for flagging this comment. moderators will review it immediately')
    return redirect(comment.content_object.get_absolute_url())
