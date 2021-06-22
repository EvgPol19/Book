from django.db import models
from django.contrib.auth import get_user_model
from book import models as book_models
User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='carts',
        verbose_name='Cart',
        on_delete=models.PROTECT
        )
    def __str__(self):
        return f'{self.pk}'



class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        verbose_name='Cart',
        related_name='goods'
    )
    book = models.ForeignKey(
        'book.Book',
        on_delete=models.PROTECT,
        verbose_name='Book'
    )
    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1
    )
    unit_price = models.DecimalField(
        verbose_name='Unit price',
        max_digits=5,
        decimal_places=2,
    )

    def __str__(self):
        return f'{self.book.name}, {self.quantity}'
