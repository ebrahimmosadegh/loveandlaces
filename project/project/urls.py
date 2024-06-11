"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import header, footer, home_page, about_page, handler404, handler500
from project import settings

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('about/', about_page, name='about'),
    path('', include('contact.urls')),
    path('', include('termsandconditions.urls')),
    path('', include('flowerwall.urls')),
    path('', include('promotion.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Use ckeditor URLs
]

# handle 404 and 500 error
handler404 = handler404
handler500 = handler500

if settings.DEBUG:
    # add root statice files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
