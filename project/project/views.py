from django.views.generic import ListView
from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')

def header(request, *args, **kwargs):
    return render(request, 'shared/header.html')

def footer(request, *args, **kwargs):
    return render(request, 'shared/footer.html')

def about_page(request):
    return render(request, 'about.html')

