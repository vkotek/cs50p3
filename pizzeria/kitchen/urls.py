from django.urls import path

from . import views

app_name = 'kitchen'
urlpatterns = [
    path('kitchen', views.kitchen_orders, name='kitchen'),
]
