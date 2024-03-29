from django.db import models

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



