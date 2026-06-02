from django.contrib import admin
from product.models import Product, Category,Review,ProductImage

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(ProductImage)
