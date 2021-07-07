"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from forms import urls, views as forms
from book import urls, views as book
from customer import views as customer_views

urlpatterns = [
    path('s-admin/', admin.site.urls),
    path('form/', include('forms.urls', namespace='forms')),
    path('book/', include('book.urls', namespace='book')),
    path('customer/', include('customer.urls', namespace='customer')),
    path('cart/', include('carts.urls', namespace='carts')),
    path('order/', include('orders.urls', namespace='orders')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('', book.Home.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


