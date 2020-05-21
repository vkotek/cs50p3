from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from eshop.models import Order, OrderLine, MenuItem

# Create your views here.

@staff_member_required(login_url='/user/')
def kitchen_orders(request):

    orders = Order.objects.filter()
    context = {
        'orders': orders,
    }
    return render(request, 'kitchen/orders.html', context)
