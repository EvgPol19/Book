from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from . import models, forms

# Create your views here.
class OrderCreate(FormView):
    form_class = forms.OrderCreateForm
    template_name = 'orders/order_create.html'
    success_url = reverse_lazy('orders:thanks')

    def get_initial(self):
        if self.request.user.is_anonymous:
            return {}
        country = self.request.user.customer.country
        city = self.request.user.customer.city
        phone = self.request.user.customer.phone
        address = self.request.user.customer.аddress_1
        other = self.request.user.customer.other

        return {
            'country': country,
            'city': city,
            'address': address,
            'phone': phone,
            'other': other
        }


    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id') #словареподобный объект
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
            defaults={},
            )
        if created:
            return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))
        address = form.cleaned_data.get('address')
        phone = form.cleaned_data.get('phone')
        order = models.Order.objects.create(
            cart=cart,
            address=address,
            phone=phone

        )
        self.request.session.delete('cart_id')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id') #словареподобный объект
        cart, created = models.Cart.objects.get_or_create(
            pk = cart_id,
            defaults={},
            )
        context['object'] = cart
        return context

class Thanks(TemplateView):
    template_name = 'orders/thanks.html'