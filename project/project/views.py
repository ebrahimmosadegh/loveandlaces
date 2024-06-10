from django.views.generic import ListView
from django.shortcuts import render

from flowerwall.models import FlowerWall


def home_page(request):
    flowers = FlowerWall.objects.all()
    context= {
        'flowers': flowers
    }
    return render(request, 'index.html', context)

def header(request, *args, **kwargs):
    return render(request, 'shared/header.html')

def footer(request, *args, **kwargs):
    return render(request, 'shared/footer.html')

def about_page(request):
    return render(request, 'about.html')

