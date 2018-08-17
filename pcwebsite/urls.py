"""pcwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import django_cas_ng.views as cas_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('manage/', admin.site.urls),
    path('login/', cas_views.login, name='cas_ng_login'),
    path('logout/', cas_views.logout, name='cas_ng_logout'),
    path('accounts/callback', cas_views.callback, name='cas_ng_proxy_callback'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)