from django.contrib import admin

from .models import Item, Topping, Category, Size

# Register your models here.

admin.site.register(Item)
admin.site.register(Topping)
admin.site.register(Category)
admin.site.register(Size)