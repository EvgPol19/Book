from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('create_order/', views.OrderCreate.as_view(), name='create_order'),
    path('customer_order_list/', views.CustomerOrderListView.as_view(), name='customer_order_list'),
    path('customer_order_detail/', views.CustomerOrderDetailView.as_view(), name = 'customer_order_detail'),
    path('customer_order_update/', views.CustomerOrderUpdateView.as_view(), name = 'customer_order_update'),
    path('customer_cancel_order/<int:pk>/', views.CustomerCancelOrder.as_view(), name='customer_cancel_order'),
    path('manager_order_list/', views.ManagerOrderListView.as_view(), name = 'manager_order_list'),
    path('manager_order_detail/<int:pk>/', views.ManagerOrderDetailView.as_view(), name = 'manager_order_detail'),
    path('manager_order_update/<int:pk>/', views.ManagerOrderUpdateView.as_view(), name = 'manager_order_update'),
    path('manager_cancel_order/<int:pk>/', views.ManagerCancelOrder.as_view(), name='manager_cancel_order'),
]