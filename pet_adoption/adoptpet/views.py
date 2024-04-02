from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Adopt, CartItem, AdoptionApplication
from django.contrib.auth.models import User
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

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


@login_required
def add_to_cart(request, pet_id):
    pet = Adopt.objects.get(pk=pet_id)

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, adopt_item=pet)    
        if cart_items.exists():
            cart_item = cart_items.first()
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(user=request.user, adopt_item=pet)
        return redirect('cart')
    else:
        return redirect('login')

@login_required   
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = cart_items.count()
    total_price = sum(item.adopt_item.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items, 
        'total_price': total_price,
        'total_items': total_items
    }
    return render(request, 'cart.html', context)

@login_required
def delete_from_cart(request, cart_item_id):
  cart_item = CartItem.objects.get(pk=cart_item_id)
  if cart_item.user == request.user:
      cart_item.delete()
  return redirect('cart')

@login_required
def checkout(request):
  cart_items = CartItem.objects.filter(user=request.user)
  total_price = sum(item.adopt_item.price * item.quantity for item in cart_items)

  host = request.get_host()

  paypal_checkout = {
      'business':settings.PAYPAL_RECEIVER_EMAIL,
      'amount': total_price,
      'item_name': "Adopted Item Fees",
      'invoice': uuid.uuid4(),
      'currency_code': 'USD',
      'notify_url': f"https://{host}{reverse('paypal-ipn')}",
      'return_url': f"http://{host}{reverse('adoption_successful')}",
      'cancel_url': f"http://{host}{reverse('checkout_error')}"
  }

  paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

  context = {'cart_items': cart_items, 
             'total_price': total_price,
             'paypal':paypal_payment
             }
  return render(request, 'checkout.html', context)


def submit_adoption(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phonenumber = request.POST.get('phonenumber')
        county = request.POST.get('county')
        state = request.POST.get('state')
        payment_method = request.POST.get('payment_method')

        adoption_app = AdoptionApplication.objects.create(
            user= request.user,
            first_name = first_name,
            last_name=last_name,
            email=email,
            address= address,
            phonenumber=phonenumber,
            county=county,
            state=state,
            payment_method = payment_method,
        )
        print(f"Adoption application submitted for: {adoption_app}")

        CartItem.objects.filter(user=request.user).delete()
        return redirect('order')
    else:
        return redirect('cart')


def about(request):
    context = {

    }
    return render(request, 'about.html', context)

def contact(request):
    context = {

    }
    return render(request, 'contact.html', context)

def donate(request):
    # Define donation amounts
    donation_amounts = [
        {'amount': 20, 'description': 'Help provide food and shelter for a pet in need.'},
        {'amount': 50, 'description': 'Contribute to medical care and vaccinations for rescued animals.'},
        {'amount': 100, 'description': 'Sponsor the adoption fee for a pet, making it easier for them to find a loving family.'},
    ]

    # Create PayPal donation forms for each amount
    paypal_donation_forms = []
    for donation in donation_amounts:
        paypal_checkout = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': donation['amount'],
            'item_name': 'Pet Adoption Donation',
            'currency_code': 'USD',
            'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
            'return_url': request.build_absolute_uri(reverse('donation_successful')),
            'cancel_return': request.build_absolute_uri(reverse('donation_cancel')),
        }
        paypal_donation_forms.append(PayPalPaymentsForm(initial=paypal_checkout))

    context = {'donation_amounts': zip(donation_amounts, paypal_donation_forms)}
    return render(request, 'donate.html', context)


    
def adoption_successful(request):
    
        return render(request, 'adoption_successful.html')
def checkout_error(request):
    
        return render(request, 'checkout_error.html')

def donation_successful(request):
    
        return render(request, 'donation_successful.html')

def donation_cancel(request):
    
        return render(request, 'donation_cancel.html')

def order(request):
    context = {

    }
    return render(request, 'order.html', context)