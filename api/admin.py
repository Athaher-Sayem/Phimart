from django.contrib import admin
from order.models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user']




admin.site.register(CartItem)
