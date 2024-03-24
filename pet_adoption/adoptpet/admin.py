from django.contrib import admin
from .models import Adopt


class AdoptAdmin(admin.ModelAdmin):
    fields = ('name', 'date_added', 'age','month_year', 'description', 'image', 'price', 'category')
    list_display = ('id', 'name', 'age', 'month_year', 'date_added', 'price', 'category')
    ordering =('-id',)
    readonly_fields = ('date_added',)
    search_fields = ('name', 'date_added', 'age', 'category')
    list_per_page= 15

admin.site.register(Adopt, AdoptAdmin)


# admin.py
from django.contrib import admin

admin.site.site_header = "Pet Adoption Management System"
admin.site.site_title = "Pet Adoption Admin Panel"
admin.site.index_title = "Welcome to the Pet Adption Admin Panel"
