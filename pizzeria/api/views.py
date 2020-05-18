from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from .serializers import MenuItemSerializer, OrderLineSerializer, CartSerializer, ToppingsSerializer
from eshop.models import MenuItem, OrderLine, ItemTopping

from rest_framework import status
# from rest_framework.decorators import api_view, action
from rest_framework.response import Response

# Create your views here.

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by('name')
    serializer_class = MenuItemSerializer

class OrderLineViewSet(viewsets.ModelViewSet):

    queryset = OrderLine.objects.filter(order_id__isnull=True).order_by('id')
    serializer_class = OrderLineSerializer


    # Get items in cart
    def list(self, request):
        print('OrderLineViewSet.list()')
        data = OrderLine.objects.filter(order_id__isnull=True, customer=request.user).order_by('item')
        
        return Response(data.values())

    # Add to cart
    def create(self, request):

        customer = request.user
        item = MenuItem.objects.get(id=request.data['item'])

        if item.toppings and not request.data.get('toppings'):
            return Response(status=202, data={'message': 'Toppings missing or incorrect number of toppings selected.'})


        new_line = OrderLine.objects.create(customer=customer, item=item, price=item.price)

        if request.data.get('toppings'):
            print(request.data.get('toppings'))

            try:
                toppings = request.data.getlist('toppings')
            except:
                print('topipings in a QueryDict')

            try:
                toppings = request.data.get('toppings')
            except:
                print('topipings in a QueryDict')

            for topping_id in toppings:
                topping = ItemTopping.objects.get(pk=topping_id)
                print("Adding topping:", topping_id, topping)
                new_line.toppings.add(topping)
                new_line.price = new_line.price + topping.price
                new_line.save()

        data = OrderLine.objects.filter(order_id__isnull=True, customer=request.user).order_by('item')

        return Response(data.values())

    def destroy(self, request, pk=None):
        print('OrderLineViewSet.destroy()')
        result = OrderLine.objects.get(pk=pk).delete()
        print(result)
        return Response("OK!")
    
class CartViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = OrderLine.objects.filter(order_id__isnull=True ).order_by('item')
    serializer_class = CartSerializer

class ToppingsViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ItemTopping.objects.all()
    serializer_class = ToppingsSerializer

    def list(self, request):
        topping_options = ItemTopping.objects.all()
        return Response(topping_options.values())

    def retrieve(self, request, pk):
        category_id = MenuItem.objects.get(pk=pk).category.id
        topping_options = ItemTopping.objects.filter(allowed_categories__in=[category_id])

        return Response(topping_options.values())
