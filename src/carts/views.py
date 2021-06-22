from django.views.generic import DetailView
from . import models
from book import models as book_models


class CartDetailView(DetailView):
    template_name = 'carts/cart_detail.html'
    model = models.Cart

    def get_object(self, queryset=None):
        # cart
        cart_id = self.request.session.get('cart_id') #словареподобный объект
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
            defaults={},
        )
        if created:
            self.request.session['cart_id'] = cart.pk
        # book in cart
        book_id = self.request.GET.get('book_id')
        if book_id:
            book = book_models.Book.objects.get(pk = int(book_id))
            book_in_cart, book_created = models.BookInCart.objects.get_or_create(
                cart = cart,
                book = book,
                defaults={
                    'unit_price': book.price
                },
            )
            if not book_created:
                # если товар был в корзине
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
                book_in_cart.save()
        return cart
