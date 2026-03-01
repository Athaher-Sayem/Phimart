from django.shortcuts import render
from order.serializers import CartSerializer
from rest_framework.viewsets import GenericViewSet
from order.models import Cart
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
# Create your views here.




class CartViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer