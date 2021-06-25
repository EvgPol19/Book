from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='customer',
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name='Phone',
        max_length=13
    )
    country = models.CharField(
        verbose_name='Country',
        max_length=35,
        blank=True,
        null=True,
        default='No record'
    )
    city = models.CharField(
        verbose_name='City',
        max_length=35,
        blank=True,
        null=True,
        default='No record'
    )
    postcode = models.CharField(
        verbose_name='Postcode',
        max_length=10,
        blank=True,
        null=True,
        default='No record'
    )
    аddress_1 = models.CharField(
        verbose_name='Address 1',
        max_length=150,
        blank=True,
        null=True,
        default='No record'
    )
    address_2 = models.CharField(
        verbose_name='Address 2',
        max_length=150,
        blank=True,
        null=True,
        default='No record'
    )
    other = models.TextField(
        verbose_name='Other information',
        max_length=200,
        blank=True,
        null=True,
        default='No record'
    )
    def __str__(self) -> str:
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('user_update', kwargs={'pk': self.pk})