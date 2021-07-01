from django.db import models
from carts.models import Cart
from forms.models import StatusOrder

# Create your models here.


class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete = models.PROTECT,
        verbose_name = 'Order',
        related_name = 'order'
    )
    country = models.CharField(
        verbose_name='Country',
        max_length=35,
        blank = False,
        null = False,
        default='No record'
    )
    city = models.CharField(
        verbose_name='City',
        max_length=35,
        blank = False,
        null = False,
        default='No record'
    )
    address = models.CharField(
        verbose_name = 'Address',
        max_length=150,
        blank = False,
        null = False,
        default='No record'
    )
    phone = models.CharField(
        verbose_name = 'Phone',
        max_length=20,
        blank = False,
        null = False,
        default='No record'
    )
    other = models.TextField(
        verbose_name='Other information',
        max_length=200,
        blank=True,
        null=True,
        default='No record'
    )
    created = models.DateTimeField(
        verbose_name='order created',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='order updated',
        auto_now=True,
        auto_now_add=False
    )
    status = models.ForeignKey(
        StatusOrder,
        on_delete=models.PROTECT,
        related_name='status_orders',
        default=1
    )
    def __str__(self) -> str:
        return f'{self.phone}'
