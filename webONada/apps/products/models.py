from django.db import models
from apps.users.models import User

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='products')
    

    def __str__(self):
        return self.name
    
class ProductPresentation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='presentations')
    featured_title = models.CharField(max_length=255, blank=True, null=True, help_text="Featured title for the sales page")
    short_description = models.TextField(blank=True, null=True, help_text="Short description for previews")
    featured_image = models.ImageField(upload_to='products/', blank=True, null=True, help_text="Featured image for the main page")
    order = models.IntegerField(default=0, help_text="Order in which the product will appear on the page")
    featured = models.BooleanField(default=False, help_text="Should this product be featured on the main page?")
    publication_date = models.DateTimeField(auto_now_add=True, help_text="Date when the product was published on the page")
    active = models.BooleanField(default=True, help_text="Is this product active?")
    stock = models.IntegerField(default=0, help_text="Stock available for this product")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Price for this product")
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Product Presentation"
        verbose_name_plural = "Product Presentations"

    def __str__(self):
        return f"Presentation of {self.product.name}"
    
class ProductRating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(help_text="Rating value from 1 to 5")
    review = models.TextField(blank=True, null=True, help_text="Optional review text")
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        unique_together = ('product', 'user')
        ordering = ['-created_at']
        verbose_name = "Product Rating"
        verbose_name_plural = "Product Ratings"

    def __str__(self):
        return f"{self.product.name} - {self.rating} by {self.user.username}"