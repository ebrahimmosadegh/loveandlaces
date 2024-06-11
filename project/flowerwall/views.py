from django.shortcuts import render, get_object_or_404
from .models import FlowerWall, Gallery

# Create your views here.
def flowerwall(request, slug):
    flower = get_object_or_404(FlowerWall , slug=slug)
    galleries = Gallery.objects.filter(flowerwall_id=flower.pk)
    context ={
'flower':flower,
'galleries': galleries
    }
    return render(request,'flowerwall.html',context)

def flower_list(request):
    flowers = FlowerWall.objects.all()
    context= {
        'flowers': flowers
    }
    return render(request, 'flowerwalls.html', context)