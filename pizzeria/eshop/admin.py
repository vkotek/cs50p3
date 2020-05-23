from django.contrib import admin

from django.forms import ModelForm

from .models import \
    Order, \
    OrderLine, \
    PaymentMethod, \
    MenuItem, \
    ItemTopping, \
    Category, \
    Size

# Register your models here.

admin.site.register(PaymentMethod)
admin.site.register(MenuItem)
admin.site.register(ItemTopping)
admin.site.register(Category)
admin.site.register(Size)

class OrderLineAdmin(admin.ModelAdmin):
    list_display  = ['customer', 'customer', 'item', 'price']
    search_fields = ['customer']

admin.site.register(OrderLine, OrderLineAdmin)

class OrderlineInline(admin.StackedInline):
    model = OrderLine
    extra = 5

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'customer', 'order_date', 'completed_date', 'total_price']
    inlines = [OrderlineInline]

admin.site.register(Order, OrderAdmin)
