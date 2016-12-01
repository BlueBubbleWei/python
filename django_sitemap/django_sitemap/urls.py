"""django_sitemap URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from mysitemap.models import Entry


sitemaps={
    'mysitemap':GenericSitemap({'queryset':Entry.objects.all(),
    'date_field':'pub_date'},priority=0.6),
}



urlpatterns = [
    url(r'sitemap\.xml$',sitemap,{'sitemaps':sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/', admin.site.urls),
]
