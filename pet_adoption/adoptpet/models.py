from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Adopt(models.Model):
    pet_choice_category = (
        ("dogs", "dogs"),
        ('cats', 'cats')

    )
    months_years = (
        ("years", "years"),
        ("months", "months")
    )
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    age = models.PositiveIntegerField()
    description = models.TextField()
    breed = models.CharField(max_length=100, blank=True)
    species = models.CharField(choices=pet_choice_category, max_length=120)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(default='defaultpet.jpeg', upload_to='Adopt_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    month_year = models.CharField(choices=months_years, max_length=120)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Adopt'
        db_table = 'pets'


class CartItem(models.Model):
    adopt_item = models.ForeignKey(Adopt, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity}x {self.adopt_item.name}"

    class Meta:
        verbose_name_plural = 'CartItem'
        db_table = 'cart items'

from django.db import models
from django.contrib.auth.models import User

class AdoptionApplication(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  pet = models.ForeignKey('Adopt', on_delete=models.CASCADE, null=True, blank=True)  # Optional association with specific pet
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField()
  address = models.TextField()
  state = models.CharField(max_length=100)
  county = models.CharField(max_length=100)
  phonenumber = models.CharField(max_length=20, null=True)
  payment_method = models.CharField(max_length=50)
  status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
  created_at = models.DateTimeField(auto_now_add=True)
  paypal_transaction_id = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return f"{self.full_name} - {self.pet}"  # Example string representation
