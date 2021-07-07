from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user',
        'phone',
        'country',
        'city',
        'аddress_1',
        'postcode',
        'other',]

admin.site.register(Profile, ProfileAdmin)
