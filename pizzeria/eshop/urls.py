from django.urls import path

from . import views

app_name = 'eshop'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('cart', views.shopping_cart, name='cart'),
]
