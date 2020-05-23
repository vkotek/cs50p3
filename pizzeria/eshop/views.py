from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Order, OrderLine, MenuItem, Category

# Create your views here.

@login_required(login_url='/user/')
def shopping_cart(request):
    # Find all items in details without parent order and with user's ID
    user_id = request.user.id
    cart = OrderLine.objects.filter(customer=user_id)
    orders = Order.objects.filter(customer_id=user_id)
    context = {
        'cart': cart,
        'orders': orders,
    }
    return render(request, 'eshop/cart.html', context)

@login_required(login_url='/user/')
def orders(request):

    cart = OrderLine.objects.filter(customer=user_id)

    return render(request, 'eshop/cart.html', context)

@login_required(login_url='/user/')
def menu(request):
    context = {
        'menu': {},
    }

    items = MenuItem.objects.all()

    # Merge items with different sizes by name?
    items_merged = []


    # Sort items by category
    categories = { x.category_id for x in items } 
    for category in categories:
        category_name = Category.objects.get(pk=category).name
        context['menu'][category_name] = items.filter(category_id = category)

    return render(request, 'eshop/index.html', context)
