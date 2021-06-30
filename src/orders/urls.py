from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('create_order/', views.OrderCreate.as_view(), name='create_order'),
    path('customer_order_list/', views.CustomerOrderListView.as_view(), name='customer_order_list'),
    path('customer_order_detail/<int:pk>/', views.CustomerOrderDetailView.as_view(), name = 'customer_order_detail'),
    path('customer_order_update/<int:pk>/', views.CustomerOrderUpdateView.as_view(), name = 'customer_order_update'),
    path('customer_order_delete/<int:pk>/', views.CustomerOrderDeleteView.as_view(), name = 'customer_order_delete'),
    path('manager_order_list/', views.ManagerOrderListView.as_view(), name = 'manager_order_list'),
    path('manager_order_detail/<int:pk>/', views.ManagerOrderDetailView.as_view(), name = 'manager_order_detail'),
    path('manager_order_update/<int:pk>/', views.ManagerOrderUpdateView.as_view(), name = 'manager_order_update'),
    path('manager_order_delete/<int:pk>/', views.ManagerOrderDeleteView.as_view(), name = 'manager_order_delete'),
    path('thanks/', views.Thanks.as_view(), name='thanks'),
]