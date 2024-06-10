from django.shortcuts import render
from .models import termsAndConditions
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def terms_conditions_page(request):
    try:
        context ={
            'query': termsAndConditions.objects.get()
        }
        return render(request, 'terms_conditions.html',context)
    except ObjectDoesNotExist:
        pass
    