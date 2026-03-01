from django.urls import path
from product import views
urlpatterns = [
    path('', views.ProductsList.as_view() , name='products-list'),
    path('<int:id>/', views.ProductDetails.as_view() , name='products-list')
]
