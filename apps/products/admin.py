from django.contrib import admin
from .models import Product, Category
from .models import Product, Category, Tag, ProductImage, ProductPresentation, ProductPresentationImage

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ProductImage)
admin.site.register(ProductPresentation)
admin.site.register(ProductPresentationImage)
