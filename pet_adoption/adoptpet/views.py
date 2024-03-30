from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Adopt


def index(request):
    context = {
        'pets':Adopt.objects.all()
    }
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


def cart(request):
    
    context = {}
    return render(request, 'cat.html', context)

@login_required
def checkout(request):

    context = {

    }
    return render(request, 'checkout.html', context)


def about(request):
    context = {

    }
    return render(request, 'about.html', context)

def contact(request):
    context = {

    }
    return render(request, 'contact.html', context)

def donate(request):
    
        return render(request, 'donate.html')
    

def order(request):
    context = {

    }
    return render(request, 'order.html', context)