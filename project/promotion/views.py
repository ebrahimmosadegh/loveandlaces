from django.shortcuts import render, get_object_or_404

from .models import Promotion

# Create your views here.
def promotion(request, slug):
    promotion = get_object_or_404(Promotion , slug=slug)
    return render(request,'promotion.html', {'promotion':promotion})


