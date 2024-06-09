from django.urls import path

from .views import terms_conditions_page

urlpatterns = [
    path('terms-conditions/', terms_conditions_page, name='terms-conditions'),
]