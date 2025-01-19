from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sku = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('1', 'Main'),
        ('2', 'Secondary'),
        ('3', 'Banner'),
    ]
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    image_type = models.CharField(max_length=10, choices=IMAGE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.product.name} - {self.image_type}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='products')

    def __str__(self):
        return self.name