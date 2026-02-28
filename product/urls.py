from django.urls import path
from product import views
urlpatterns = [
    path('products/', views.view_product , name='products-list')
]
