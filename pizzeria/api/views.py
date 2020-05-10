from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MenuItemSerializer, OrderLineSerializer, CartSerializer
from eshop.models import MenuItem, OrderLine

from rest_framework import status
# from rest_framework.decorators import api_view, action
from rest_framework.response import Response

# Create your views here.

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by('name')
    serializer_class = MenuItemSerializer

class OrderLineViewSet(viewsets.ModelViewSet):

    queryset = OrderLine.objects.filter(order_id__isnull=True ).order_by('item')
    serializer_class = OrderLineSerializer


    def list(self, request):
        data = OrderLine.objects.filter(order_id__isnull=True, customer=request.user).order_by('item')
        print(data)
        
        return Response(data.values())

    def create(self, request):

        customer = request.user
        item = MenuItem.objects.get(id=request.data['item'])
        # toppings = request.data['toppings']
        OrderLine.objects.create(customer=customer, item=item)
        data = OrderLine.objects.filter(order_id__isnull=True, customer=request.user).order_by('item')
        return Response(data)

    def destroy(self, request, pk=None):
        print("Destroying something!!")
        pass
    
class CartViewSet(viewsets.ModelViewSet):

    queryset = OrderLine.objects.filter(order_id__isnull=True ).order_by('item')
    serializer_class = CartSerializer
    