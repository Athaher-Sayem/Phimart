from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product,Category
from rest_framework import status

@api_view()
def view_specific_product(request,id):
    try:
        product = Product.objects.get(pk=id)
        product_dict = {
        'id': product.id , 'name' : product.name , 'price':product.price
        }
        return Response(product_dict)
    except Product.DoesNotExist:
        return Response({'message':"Product does not exists"},status=404)

@api_view()
def view_category(request):
    return Response({'message':'Okey'})