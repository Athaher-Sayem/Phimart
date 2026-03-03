from rest_framework import serializers
from order.models import Cart, CartItem , Order,OrderItem
from product.serializers import ProductSerializer
from product.models import Product


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id','name','price']
    


class CartItemSerializer(serializers.ModelSerializer):
    # product_price=serializers.SerializerMethodField(method_name='get_product_price')
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = CartItem
        # fields = ['id', 'product','quantity','product_price']
        fields = ['id', 'product','quantity','product','total_price']


    def get_total_price(self, cart_item : CartItem):
        return cart_item.quantity * cart_item.product.price

    # def get_product_price(self , cart_item):
    #     return cart_item.product.price


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True,read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart
        fields = ['id','user','items','total_price']

    def get_total_price(self , cart : Cart):
        # list = sum([item.product.price * item.quantity for item in cart.items.all()])
        # print("list",list)
        return sum([item.product.price * item.quantity for item in cart.items.all()])


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    class Meta:
        model = CartItem
        fields = ['id','product_id','quantity']

    def save(self ,**kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try :
            cart_item = CartItem.objects.get(cart_id=cart_id,product_id=product_id)
            cart_item.quantity += quantity
            self.instance = cart_item.save()
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id , **self.validated_data)    

        return self.instance 
    
    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f"Product with id {value} does not exists")
        return value 
    


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta :
        model = CartItem
        fields = ['quantity']


class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta :
        model = OrderItem
        fields = ['id','product','quantity','total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta :
        model = Order
        fields = ['id', 'user','status','total_price','created_at','items']