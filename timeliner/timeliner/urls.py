"""ecoway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, serializers, viewsets
from django.contrib.flatpages import views
from django.contrib.staticfiles import views
from rest_framework.authtoken import views as tokenView


urlpatterns = [

re_path(r'^admin_tools/', include('admin_tools.urls')),
path('admin/', admin.site.urls),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
re_path(r'^api-token-auth/', tokenView.obtain_auth_token),
path('', include('events.urls')),
path('', include('django.contrib.flatpages.urls')),
]


if settings.DEBUG:
	urlpatterns += [re_path(r'^static/(?P<path>.*)$', views.serve)]
	# urlpatterns += [re_path(r'^media/(?P<path>.*)$', views.serve)]

	# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	# urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
