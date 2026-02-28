from django.urls import path
from product import views
urlpatterns = [
    path('', views.view_product , name='products-list')
]
