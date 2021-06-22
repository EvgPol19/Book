from django.contrib import admin
from . import models
# Register your models here.
class CartdAdmin(admin.ModelAdmin):
    list_display = ['pk',]

class BookInCartdAdmin(admin.ModelAdmin):
    list_display = [
        'book',
        'cart',
        'book',
        'quantity',
        'unit_price']

admin.site.register(models.BookInCart, BookInCartdAdmin)
admin.site.register(models.Cart, CartdAdmin)