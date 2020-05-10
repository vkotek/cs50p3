from rest_framework import serializers
from eshop.models import MenuItem, Size, Category, OrderLine

class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    size_name = serializers.CharField(source='size.name')
    class Meta:
        model = MenuItem
        fields = ( 'id', 'name', 'price', 'toppings', 'size_name', 'category_name')

class OrderLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderLine
        fields = ('customer','order_id', 'item', 'toppings')


class CartSerializer(serializers.ModelSerializer):

    item_name = serializers.CharField(source='item.name')
    item_category = serializers.CharField(source='item.category')
    item_price = serializers.CharField(source='item.price')

    class Meta:
        model = OrderLine
        fields = ('id', 'item_name', 'item_category', 'item_price', 'toppings')

    