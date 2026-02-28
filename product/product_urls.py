from django.urls import path
from product import views
urlpatterns = [
    path('<int:id>/', views.view_specific_product , name='products-list')
]
