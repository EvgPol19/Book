from django.shortcuts import render
from django.views.generic import FormView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms
from carts.models import Cart

# Create your views here.
#______________order______________
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

#______________customers view______________
class CustomerOrderListView(LoginRequiredMixin, ListView):
    model = models.Order
    template_name = 'orders/customer_order_list.html'
    def get_queryset(self):
        customer_phone = self.request.user.customer.phone
        current_customer_orders = models.Order.objects.filter(phone = customer_phone)
        return current_customer_orders

class CustomerOrderDetailView(LoginRequiredMixin, DetailView):
    model = models.Order
    template_name = 'orders/customer_order_detail.html'

class CustomerOrderUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Order
    fields = ['country', 'city', 'address', 'phone', 'other']
    template_name = 'orders/customer_order_update.html'
    success_url = reverse_lazy('orders:customer_order_list')

class CustomerOrderDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Order
    template_name = 'orders/customer_order_delete.html'
    success_url = reverse_lazy('orders:customer_order_list')

#______________managers views______________
class ManagerOrderListView(ListView):
    model = models.Order
    template_name = 'orders/manager_order_list.html'

class ManagerOrderDetailView(DetailView):
    model = models.Order
    template_name = 'orders/manager_order_detail.html'

class ManagerOrderUpdateView(UpdateView):
    model = models.Order
    template_name = 'orders/manager_order_update.html'
    success_url = reverse_lazy('orders:manager_order_list')
    fields = ['country', 'city', 'address', 'phone', 'other']

class ManagerOrderDeleteView(DeleteView):
    model = models.Order
    template_name = 'orders/manager_order_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('orders:manager_order_list')
        cart_on_delete = Cart.objects.filter(pk = self.object.pk)
        self.object.delete()
        cart_on_delete.delete()
        return HttpResponseRedirect(success_url)

#______________thanks______________
class Thanks(TemplateView):
    template_name = 'orders/thanks.html'