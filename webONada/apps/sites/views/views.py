from django.shortcuts import render
from apps.products.models import Product, Category, ProductPresentation, ProductImage, ProductPresentationImage

# Create your views here.
def home(request):

    """
    Render the home page.
    """
    

    pictures_banner = ProductPresentationImage.objects.select_related(
        'product'
    ).filter(image_type='3').order_by('id')

    categories = Category.objects.all()

    featured_presentations = ProductPresentation.objects.filter(featured=True, active=True)

    context = {
        'pictures_banner': pictures_banner,
        'categories' : categories,
        'featured_presentations': featured_presentations,
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