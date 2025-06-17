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
    categories = Category.objects.all()

    context = {
        'form': form,
        'products': products,
        'categories': categories,
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

#site categories
def categories(request):
    """
    Render the categories page.
    """
    # listado de categorias
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/categories.html', context)

#site categories details
def categories_detail(request, pk):
    """
    Render the categories detail page.
    """
    # listado de categorias
    category = Category.objects.get(id=pk)

    context = {
        'category': category,
    }

    return render(request, 'products/categories_detail.html', context)