from django.contrib import admin

from .models import \
    Order, \
    OrderLine, \
    PaymentMethod, \
    MenuItem, \
    ItemTopping, \
    Category, \
    Size

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(PaymentMethod)
admin.site.register(MenuItem)
admin.site.register(ItemTopping)
admin.site.register(Category)
admin.site.register(Size)
