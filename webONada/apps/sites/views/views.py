from django.shortcuts import render
from apps.products.models import Product, Category, ProductPresentation, ProductImage

# Create your views here.
def home(request):

    """
    Render the home page.
    """
    pictures_banner = ProductImage.objects.filter(image_type='3').order_by('id')
    
    context = {
        'pictures_banner': pictures_banner,
    }

    return render(request, 'home.html', context)

# site about
def about(request):
    return render(request, 'about.html')

# site products
def products(request):
    return render(request, 'products.html')

# site productsDetail
def productsDetail(request):
    return render(request, 'productsDetail.html')

# site contact
def contact(request):
    return render(request, 'contact.html')