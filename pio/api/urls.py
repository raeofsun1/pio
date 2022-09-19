"""pio URL Configuration

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
from django.urls import path
from api import views

urlpatterns = [
    path('',views.index,name='index'),
    path('product_list/',views.product_list,name='product_list'),
    path('product_create/',views.product_create,name='product_create'),
    path('product_delete/<int:pk>/',views.product_delete,name='product_delete'),
    path('seller_list/',views.seller_list,name='seller_list'),
    path('seller_create/',views.seller_create,name='seller_create'),
    path('seller_delete/<int:pk>/',views.seller_delete,name='seller_delete'),
    path('product_seller_list/',views.product_seller_list,name='product_seller_list'),
    path('product_seller_create/',views.product_seller_create,name='product_seller_create'),
    path('product_seller_delete/<int:pk>/',views.product_seller_delete,name='product_seller_delete'),
    path('address_list/',views.address_list,name='address_list'),
    path('address_create/',views.address_create,name='address_create'),
    path('address_delete/<int:pk>/',views.address_delete,name='address_delete'),
    path('user_list/',views.user_list,name='user_list'),
    path('user_create/',views.user_create,name='user_create'),
    path('user_delete/<int:pk>/',views.user_delete,name='user_delete'),
    path('user_update/<int:pk>/',views.user_update,name='user_update'),
    path('order_list/',views.order_list,name='order_list'),
    path('order_create/',views.order_create,name='order_create'),
    path('order_delete/<int:pk>/',views.order_delete,name='order_delete'),
    path('order_update/<int:pk>/',views.order_update,name='order_update'),
    path('order_seller_list/<int:pk>/',views.order_seller_list,name='order_seller_list'),
    path('order_user_list/<int:pk>/',views.order_user_list,name='order_user_list'), 
]