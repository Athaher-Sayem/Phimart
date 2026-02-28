from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def view_product(request):
    return Response({'message':'Okey'})