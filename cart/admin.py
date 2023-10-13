from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ( 'cart_id', 'date_added','id')

admin.site.register(Cart, CartAdmin)
