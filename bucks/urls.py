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

urlpatterns = [
    url(r'^faq/$', faq, name='FAQ'),
    url(r'^developers/$', developers.as_view(), name='developers'),
    url(r'^business/$', business.as_view(), name='business'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^tags/', include('tags.urls', namespace='tags')),    
    url(r'^categories/', include('categories.urls', namespace='categories')),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^services/', include('services.urls', namespace='services')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

]
