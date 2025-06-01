from django.shortcuts import render
from apps.products.forms.ProductForms import ProductFilter

#models
from apps.products.models import Product, Category, ProductPresentation

# Create your views here.
#site products
def products(request):
    """
    Render the services page.
    """
    # form de productos
    form = ProductFilter()

    # listado de productos
    products = ProductPresentation.objects.all()

    context = {
        'form': form,
        'products': products,
    }

    return render(request, 'products/products.html', context)

# site products details
def products_detail(request, pk):
    """
    Render the services page.
    """

    # listado de productos
    products = ProductPresentation.objects.get(id=pk)

    context = {
        'products': products,
    }

    return render(request, 'products/products_detail.html', context)