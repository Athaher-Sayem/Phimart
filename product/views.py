from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product,Category
from rest_framework import status
from product.serializers import ProductSerializer ,CategorySerializer
from django.db.models import Count


@api_view()
def view_products(request):
      products = Product.objects.select_related('category').all()
      serializer = ProductSerializer(products, many=True , context={'request': request})
      return Response(serializer.data)


@api_view()
def view_specific_product(request,id):
        product = get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
   

@api_view()
def view_category(request):
    categories= Category.objects.annotate(product_count=Count('products')).all()
    serializer = CategorySerializer(categories,many=True)
    return Response(serializer.data)


@api_view()
def view_specific_category(request,pk):
        category = get_object_or_404(Category,pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)