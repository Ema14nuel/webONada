from django.contrib import admin
from .models import Product, Category
from .models import Product, Category, Tag, ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ProductImage)