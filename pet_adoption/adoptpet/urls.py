from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adopt', views.adopt, name='adopt'),
    path('adopt/<int:pet_id>', views.pet_detail, name='pet_detail'),
    path('cart/<int:pet_id>', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]