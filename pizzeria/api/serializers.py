from rest_framework import serializers
from eshop.models import MenuItem, Size, Category, OrderLine, ItemTopping, Order

class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    size_name = serializers.CharField(source='size.name')
    class Meta:
        model = MenuItem
        fields = ( 'id', 'name', 'price', 'toppings', 'size_name', 'category_name')

# class OrderLineSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = OrderLine
#         fields = ('id', 'customer','order_id', 'item', 'toppings')

class OrderLineSerializer(serializers.ModelSerializer):

    # toppings = serializers.StringRelatedField(many=True)

    class Meta:
        model = OrderLine
        fields = ('id', 'customer','order_id', 'item', 'toppings')
    
    def create(self, request):

        return OrderLine.objects.filter(order_id__isnull=True, customer=request.user).order_by('item')



class ToppingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemTopping
        fields = ('name', 'price')

class CartSerializer(serializers.ModelSerializer):

    item_name = serializers.CharField(source='item.name')
    item_category = serializers.CharField(source='item.category')
    toppings = ToppingsSerializer(many=True)

    class Meta:
        model = OrderLine
        fields = ('id', 'item_name', 'item_category', 'price', 'toppings')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'customer','order_date', 'payment_method', 'completed_date', 'total_price')
    