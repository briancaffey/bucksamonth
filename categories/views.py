from django.shortcuts import render

from services.models import Service
from .models import Category
# Create your views here.

def all_categories(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'categories/all.html', context)


def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    services = Service.objects.filter(category=category)

    context = {
        'category':category,
        'services':services,
    }

    return render(request, 'categories/category_view.html', context)
