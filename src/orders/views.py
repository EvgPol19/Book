from django.shortcuts import render
from django.views.generic import FormView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from . import models, forms
from carts.models import Cart

# Create your views here.
#______________order______________
class OrderCreate(FormView):
    form_class = forms.OrderCreateForm
    template_name = 'orders/order_create.html'

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
        messages.add_message(self.request, messages.INFO, f'{self.request.user}, thank you for your order. The manager will contact you shortly.')
        return HttpResponseRedirect(reverse_lazy('home'))

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
class CustomerOrderListView(UserPassesTestMixin, ListView):
    model = models.Order
    template_name = 'orders/customer_order_list.html'
    paginate_by = 10
    def get_queryset(self):
        customer = self.request.user
        carts = customer.carts.all()
        orders = models.Order.objects.filter(cart__in=carts)
        return orders
    def test_func(self):
        return  self.request.user.is_staff or self.request.user

class CustomerOrderDetailView(UserPassesTestMixin, DetailView):
    model = models.Order
    template_name = 'orders/customer_order_detail.html'

    def test_func(self):
        return self.request.user.is_staff or self.request.user == models.Order.objects.filter(pk=self.kwargs.get('pk')).first().cart.customer

class CustomerOrderUpdateView(UserPassesTestMixin, UpdateView):
    model = models.Order
    fields = ['country', 'city', 'address', 'phone', 'other']
    template_name = 'orders/customer_order_update.html'
    success_url = reverse_lazy('orders:customer_order_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user == models.Order.objects.filter(pk=self.kwargs.get('pk')).first().cart.customer

class CustomerCancelOrder(UserPassesTestMixin, UpdateView):
    template_name = 'orders/cancel_order.html'
    model = models.Order
    fields = ('status_cancel',)
    success_url = reverse_lazy('orders:customer_order_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user == models.Order.objects.filter(pk=self.kwargs.get('pk')).first().cart.customer

#______________managers views______________
class ManagerOrderListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = models.Order
    template_name = 'orders/manager_order_list.html'
    login_url = '/custumer/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'orders.view_order'
    paginate_by = 15

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