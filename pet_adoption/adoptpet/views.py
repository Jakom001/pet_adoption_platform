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
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        breed = request.POST.get('breed')
        age = request.POST.get('age')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # validate and sve pet information
        pet = Pet.objects.create(
            name = name,
            species=species,
            breed = breed,
            age=age,
            description=description,
            image=image,
        )
        return render(request, 'donate.html')
    

def order(request):
    context = {

    }
    return render(request, 'order.html', context)