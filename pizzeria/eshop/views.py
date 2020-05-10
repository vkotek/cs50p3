from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import OrderLine, MenuItem

# Create your views here.

@login_required(login_url='/user/')
def shopping_cart(request):
    # Find all items in details without parent order and with user's ID
    user_id = request.user.id
    cart = OrderLine.objects.filter(customer=user_id)
    context = {
        'cart': cart,
    }
    return render(request, 'eshop/cart.html', context)

def create_order(request):
    return None

def menu(request):
    context = {
        'menu': MenuItem.objects.all()
    }
    return render(request, 'eshop/index.html', context)

