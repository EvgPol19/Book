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
        return f'{self.customer}'

    @property
    def total_summ(self):
        all_goods = self.goods.all()
        total = 0
        for book in all_goods:
            total += book.total_price
        return total


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
        return f'{self.book.books_name}'

    @property
    def total_price(self):
        return self.book.price * self.quantity
