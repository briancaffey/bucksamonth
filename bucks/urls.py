"""bucks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from services.views import HomeView
from accounts.views import faq, developers, business
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

# Dictionary containing your sitemap classes
sitemaps = {
   'products': ServiceSitemap(),
}

urlpatterns = [

    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/blog/', include('blog.api.urls', namespace="api-posts")),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^business/$', business.as_view(), name='business'),
    url(r'^categories/', include('categories.urls', namespace='categories')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^developers/$', developers.as_view(), name='developers'),
    url(r'^faq/$', faq, name='FAQ'),
    url(r'^services/', include('services.urls', namespace='services')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^tags/', include('tags.urls', namespace='tags')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^$', HomeView.as_view(), name='home'),

]
