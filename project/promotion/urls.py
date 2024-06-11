from django.urls import path

from .views import promotion

urlpatterns = [
    path('promotion/<slug:slug>', promotion, name='promotion'),
]