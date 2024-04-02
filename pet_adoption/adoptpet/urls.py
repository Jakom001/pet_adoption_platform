from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adopt', views.adopt, name='adopt'),
    path('adopt/<int:pet_id>', views.pet_detail, name='pet_detail'),
    path('cart', views.cart, name='cart'),
    path('add-to-cart/<int:pet_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete-from-cart/<int:cart_item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('order', views.order, name='order'),
    path('adoption_successful/', views.adoption_successful, name='adoption_successful'),
    path('checkout_error/', views.checkout_error, name='checkout_error'),
    path('donation_successful/', views.donation_successful, name='donation_successful'),
    path('donation_cancel/', views.donation_cancel, name='donation_cancel'),

]