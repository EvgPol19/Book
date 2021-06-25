from django.views.generic import DetailView, RedirectView
from django.urls import reverse
from . import models
from book import models as book_models
from . import utils


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

class RecalculateCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        current_cart_pk = self.request.session.get('current_cart_pk')
        if not current_cart_pk:
            return reverse('carts:cart_detail')
        cart_items_from_form = self.request.GET
        print(cart_items_from_form)
        action = utils.update_items_in_cart(cart_items_from_form, current_cart_pk)
        if action == "checkout":
            url = reverse('orders:checkout')
        else:
            url = reverse('carts:cart_detail')
        return url