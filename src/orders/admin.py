from django.contrib import admin
from . import models

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'cart',
        'country',
        'city',
        'address',
        'phone',
        'other',
        'status']

admin.site.register(models.Order, OrderAdmin)