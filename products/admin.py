from email.mime import image
from django.contrib import admin
from products.models import Product
from dataclasses import fields


class ProductAdmin(admin.ModelAdmin):
    fields = ('title','description','price', 'image')
    
    list_display = ('__str__','slug','created_at')
    
# Register your models here.
admin.site.register(Product, ProductAdmin)