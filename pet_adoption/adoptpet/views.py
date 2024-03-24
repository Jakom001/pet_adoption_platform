from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Adopt


def index(request):
    context = {}
    return render(request, 'index.html', context)

def  adopt(request):
    context = {
        'pets':Adopt.objects.all()
        
    }
    return render(request, 'adopt.html', context)


def pet_detail(request, pet_id):
    pet = get_object_or_404(Adopt, pk=pet_id)
    context = {'pet':pet}
    return render(request, 'pet_detail.html', context)


def cart(request, pet_id):
    pet = get_object_or_404(Adopt, pk = pet_id)
    context = {'pet':pet}
    return render(request, 'cat.html', context)

@login_required
def checkout(request):

    context = {

    }
    return render(request, 'checkout.html', context)

