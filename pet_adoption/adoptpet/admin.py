from django.contrib import admin
from .models import Adopt, AdoptionApplication


class AdoptAdmin(admin.ModelAdmin):
    fields = ('name', 'date_added', 'age','month_year', 'description','breed', 'gender', 'image', 'price', 'species')
    list_display = ('id', 'name', 'age', 'month_year', 'date_added','breed', 'gender', 'price', 'species')
    ordering =('-id',)
    readonly_fields = ('date_added',)
    search_fields = ('name', 'date_added', 'age', 'species')
    list_per_page= 15

admin.site.register(Adopt, AdoptAdmin)


class AdoptionApplicationAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'phonenumber', 'address', 'payment_method', 'county', 'state')
    list_display = ('id', 'first_name', 'phonenumber', 'payment_method', 'county', 'state')
    ordering=('-id',)
    list_per_page = 15

admin.site.register(AdoptionApplication, AdoptionApplicationAdmin)

# admin.py
from django.contrib import admin

admin.site.site_header = "Pet Adoption Management System"
admin.site.site_title = "Pet Adoption Admin Panel"
admin.site.index_title = "Welcome to the Pet Adption Admin Panel"
