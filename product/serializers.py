from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product,Review
from django.contrib.auth import get_user_model


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

    product_count=serializers.IntegerField(read_only=True)
    # product_count = serializers.SerializerMethodField(method_name='get_product_count')

    # def get_product_count(self,category):
    #     count = Product.objects.filter(category=category).count()
    #     return count





# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     unit_price = serializers.DecimalField(
#         max_digits=10, decimal_places=2, source='price')
    
#     price_with_tax= serializers.SerializerMethodField(method_name='calculate_tax')

#     # category = serializers.PrimaryKeyRelatedField(
#     #     queryset=Category.objects.all()
#     # )
#     # category = serializers.StringRelatedField()
#     # category = CategorySerializer()

#     category = serializers.HyperlinkedRelatedField(
#         queryset=Category.objects.all(),
#         view_name='view-specific-category'
#     )

#     def calculate_tax(self,product):
#         return round(product.price* Decimal(1.1),2)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'stock', 'category', 'price_with_tax']  #other 
        

    # category = serializers.HyperlinkedRelatedField(
    #         queryset=Category.objects.all(),
    #         view_name='view-specific-category'
    #      )

    price_with_tax= serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self,product):
        return round(product.price* Decimal(1.1),2)    
    
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Price could not be negative')
        return price
    
    def create(self, validated_data):
        product = Product(**validated_data)
        product.other = 1
        product.save()
        return product
    



class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_current_user_name')
    class Meta:
        model = get_user_model()
        fields = ['id','name']

    def get_current_user_name(self,obj):
        return obj.get_full_name()




class ReviewSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(read_only=True)
    user = SimpleUserSerializer()
    class Meta:
        model = Review
        fields = ['id','user','product','ratings','comment']

        read_only_fields = ['user','product']

    def create(self, validated_data ):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id,**validated_data)
        return review



