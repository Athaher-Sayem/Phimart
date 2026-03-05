from django.shortcuts import render
from order.serializers import CartSerializer,CartItemSerializer,AddCartItemSerializer,UpdateCartItemSerializer,OrderSerializer,CreateOrderSerializer , UpdateOrderSerializer,EmptySerializer
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from order.models import Cart,CartItem,Order,OrderItem
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from order.services import OrderService
# Create your views here.




class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes =[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Cart.objects.prefetch_related('items__product').filter(user=self.request.user)


class CartitemViewSet(ModelViewSet):
    http_method_names =['get','post','patch','delete']
    # queryset = CartItem
    # serializer_class=CartItemSerializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id=self.kwargs['cart_pk'])
    

class OrderViewSet(ModelViewSet):
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        return [IsAuthenticated()]

    http_method_names = ['get','post','patch','delete','head','options']

    @action(detail=True  , methods=['post'] , permission_classes=[IsAuthenticated])
    def cancel(self , request , pk=None):
        order =  self.get_object()
        OrderService.cancel_order(order=order , user=request.user)
        return Response({'Status':"Order Canceled"})



    def get_serializer_class(self):
        if self.action == 'cancel':
            return EmptySerializer
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer
    def get_serializer_context(self):
        return {'user_id': self.request.user.id , 'user': self.request.user}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user=self.request.user)