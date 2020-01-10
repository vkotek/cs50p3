from django.contrib import admin

from .models import Order, Detail, PaymentMethod

# Register your models here.

admin.site.register(Order)
admin.site.register(Detail)
admin.site.register(PaymentMethod)