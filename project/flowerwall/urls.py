from django.urls import path

from .views import flowerwall, flower_list

urlpatterns = [
    path('flowerwall/<slug:slug>', flowerwall, name='flowerwall'),
    path('flowerwalls/', flower_list, name='flowerwalls'),
]