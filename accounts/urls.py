from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_text>/', views.customer, name='customer'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<str:pk_text>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk_text>/', views.delete_order, name='delete_order'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('customer_order/<str:pk_text>/', views.customer_order, name='customer_order'),
    path('update_customer/<str:pk_text>/', views.update_customer, name='update_customer'),
    path('delete_customer/<str:pk_text>/', views.delete_customer, name='delete_customer'),
]