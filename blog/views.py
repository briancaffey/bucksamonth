from urllib.parse import quote_plus

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.text import slugify

from .models import Post
from taggit.models import Tag
from comments.models import Comment

from .forms import PostForm
from comments.forms import CommentForm

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

def index(request):
    queryset_list = Post.objects.all()
    authors = list(set([post.user for post in queryset_list]))

    context = {
        'object_list':queryset_list,
        'authors':authors,
    }

    return render(request, 'blog/index.html', context)


def detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    instance.views += 1
    instance.save()
    initial_data = {
		'content_type':instance.get_content_type,
		'object_id':instance.id
	}

    form = CommentForm(request.POST or None, initial=initial_data)
    comments = instance.comments

    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        comment_emoji = form.cleaned_data.get('emoji')
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
                        user=request.user,
                        content_type=content_type,
                        object_id=obj_id,
                        content=content_data,
                        parent=parent_obj,
                        emoji=comment_emoji,
                    )
        messages.success(request, 'Your comment was added!')
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


    context = {
        'instance':instance,
        'comments':comments,
        'form':form,
    }

    return render(request, 'blog/post_detail.html', context)

@login_required
def create(request):
	if not request.user.is_authenticated:
		raise Http404

	form = PostForm(request.POST or None)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.user = request.user
		print(form.cleaned_data.get('title'))
		instance.save()
		form.save_m2m()

		#message success
		messages.success(request, 'Successfully Created!')
		return redirect('blog:index')
	elif request.method=="POST":
		messages.error(request, "not Successfully created")

	context = {
		'form': form
	}
	return render(request, "blog/post_form.html", context)

def all_tags(request):
    return render(request, 'tags/all_tags.html', {})

def tag_view(request, slug):
    tag = Tag.objects.get(slug=slug)
    posts = Post.objects.filter(tags__name__in=[tag])
    count = len(posts)
    context = {
        'tag':tag,
        'posts': posts,
        'count':count
    }

    return render(request, 'blog/tag_view.html', context)

def author_view(request, username):
    author = User.objects.get(username=username)

    posts = Post.objects.filter(user=author)
    context = {
        'posts':posts,
        'author':author,
    }
    return render(request, 'blog/author_view.html', context)



def update(request, slug):
	instance = get_object_or_404(Post, slug=slug)
	if instance.user != request.user:
		messages.success(request, "You don't have permission to edit someone else's post.")
		return HttpResponseRedirect(instance.get_absolute_url())

	form = PostForm(request.POST or None, instance=instance)


	if form.is_valid():
		instance.user = request.user
		instance.slug = slugify(instance.title)
		instance = form.save(commit=False)

		instance.save()
		form.save_m2m()

		messages.success(request, 'Your post has been updated!')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'title':instance.title,
		'instance':instance,
		'form':form}
	return render(request, 'blog/post_update.html', context)

def delete(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    user_author = instance.user

    if request.user == user_author:
        instance.delete()
        messages.success(request, "your blog post was deleted")
        return redirect('blog:author_view', username=user_author.username)
    else:
        messages.success(request, "you don't have permission to delete this post")
        return redirect(instance.get_absolute_url())
