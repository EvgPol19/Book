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
        cart_id = self.request.session.get('cart_id')
        customer = self.request.user

        if customer.is_anonymous:
            customer = None

        cart, created = Cart.objects.get_or_create(
            pk = cart_id,
            customer = customer,
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
        del self.request.session['cart_id']
        return HttpResponseRedirect(reverse_lazy('carts:cart_detail'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id') #словареподобный объект
        customer = self.request.user

        if customer.is_anonymous:
            customer = None

        cart, created = Cart.objects.get_or_create(
            pk = cart_id,
            customer = customer,
            defaults={},
            )
        context['object'] = cart
        return context

#______________customers view______________
class CustomerOrderListView(LoginRequiredMixin, ListView):
    model = models.Order
    template_name = 'orders/customer_order_list.html'
    def get_queryset(self):
        customer = self.request.user
        carts = customer.carts.all()
        orders = models.Order.objects.filter(cart__in=carts)
        return orders

class CustomerOrderDetailView(LoginRequiredMixin, DetailView):
    model = models.Order
    template_name = 'orders/customer_order_detail.html'
    def get_object(self):

        return self.request.user


class CustomerOrderUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Order
    fields = ['country', 'city', 'address', 'phone', 'other']
    template_name = 'orders/customer_order_update.html'
    success_url = reverse_lazy('orders:customer_order_list')
    def get_object(self):
        return self.request.user.carts.goods
class CustomerCancelOrder(LoginRequiredMixin, UpdateView):
    template_name = 'orders/cancel_order.html'
    model = models.Order
    fields = ('status_cancel',)
    success_url = reverse_lazy('orders:customer_order_list')

#______________managers views______________
class ManagerOrderListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = models.Order
    template_name = 'orders/manager_order_list.html'
    login_url = '/custumer/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'orders.view_order'

class ManagerOrderDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = models.Order
    template_name = 'orders/manager_order_detail.html'
    login_url = '/custumer/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'orders.view_order'

class ManagerOrderUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = models.Order
    template_name = 'orders/manager_order_update.html'
    success_url = reverse_lazy('orders:manager_order_list')
    fields = ['country', 'city', 'address', 'phone', 'other', 'status_mng', 'status_cancel']
    login_url = '/custumer/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'orders.change_order'

class ManagerCancelOrder(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'orders/cancel_order.html'
    model = models.Order
    fields = ('status_cancel',)
    success_url = reverse_lazy('orders:manager_order_list')
    login_url = '/custumer/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'orders.change_order'


#______________thanks______________
class Thanks(TemplateView):
    template_name = 'orders/thanks.html'