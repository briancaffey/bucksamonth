from django.shortcuts import render

from services.models import Service
# Create your views here.
def all_tags(request):

    return render(request, 'tags/all_tags.html', {})



def service_tag_view(request, tag_name):
    qs = Service.objects.filter(tags__name__in=[tag_name])
    context = {
        'tag_name':tag_name,
        'qs':qs,
    }
    return render(request, 'tags/service_tag.html', context)


def blog_tag_view(request, tag_name):

    context = {
        ''
    }
