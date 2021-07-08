from django.views.generic import DetailView, RedirectView, View, RedirectView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from . import models
from book import models as book_models



class CartDetailView(DetailView):
    template_name = 'carts/cart_detail.html'
    model = models.Cart

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        customer = self.request.user

        if customer.is_anonymous:
            customer = None

        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
            customer = customer,
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

class BookInCartDeleteView(RedirectView):
    model = models.BookInCart
    success_url = reverse_lazy('carts:cart_detail')

    def get_redirect_url(self, *args, **kwargs):
        self.model.objects.get(pk=self.kwargs.get('pk')).delete()
        return self.success_url

class CartView(View):
    def post(self, request):
        action = request.POST.get('submit')
        cart_id = self.request.session.get('cart_id') #словареподобный объект
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
            defaults={},
            )
        if created:
            self.request.session['cart_id'] = cart.pk
        goods = cart.goods.all()
        if goods:
            for key, value in request.POST.items():
                if 'quantitybook_' in key:
                    pk = int(key.split('_')[1])
                    good = goods.get(pk=pk)
                    good.quantity = int(value)
                    good.save()
        if action == 'save_card':
            return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))
        elif action == 'create_order':
            return HttpResponseRedirect(reverse_lazy('orders:create_order'))
        else:
            return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))
