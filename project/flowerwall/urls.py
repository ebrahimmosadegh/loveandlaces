from django.urls import path

from .views import flowerwall

urlpatterns = [
    path('flowerwall/<slug:slug>', flowerwall, name='flowerwall'),
]