from django.views.generic import ListView
from django.shortcuts import render

from flowerwall.models import FlowerWall
from promotion.models import Promotion


def home_page(request):
    flowers = FlowerWall.objects.all()
    promotions = Promotion.objects.all()
    context= {
        'flowers': flowers,
        'promotions':promotions,
    }
    return render(request, 'index.html', context)

def header(request, *args, **kwargs):
    return render(request, 'shared/header.html')

def footer(request, *args, **kwargs):
    return render(request, 'shared/footer.html')

def about_page(request):
    return render(request, 'about.html')

def handler404(request, exception):
    return render(request, 'Error/404.html', status=404)

def handler500(request):
    return render(request, 'Error/500.html', status=500)

