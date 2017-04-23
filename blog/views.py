from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from comments.models import Comment
from .forms import PostForm
from comments.forms import CommentForm

from django.utils.text import slugify

from django.contrib.contenttypes.models import ContentType

from django.contrib import messages

# Create your views here.
def index(request):
    queryset_list = Post.objects.all()
    context = {
        'object_list':queryset_list,
    }

    return render(request, 'blog/index.html', context)


def detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)
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


def create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	if not request.user.is_authenticated:
		raise Http404

	form = PostForm(request.POST or None)

	if form.is_valid():

		instance = form.save(commit=False)
		instance.user = request.user
		print(form.cleaned_data.get('title'))
		instance.save()
		#message success
		messages.success(request, 'Successfully Created!')
		return redirect('blog:index') #HttpResponseRedirect(instance.get_absolute_url())
	elif request.method=="POST":
		messages.error(request, "not Successfully created")

	context = {
		'form': form
	}
	return render(request, "blog/post_form.html", context)


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
		messages.success(request, 'Your post has been updated!')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'title':instance.title,
		'instance':instance,
		'form':form}
	return render(request, 'blog/post_update.html', context)

def delete(request, slug):
    pass
