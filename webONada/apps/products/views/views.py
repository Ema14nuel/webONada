from django.shortcuts import render

# Create your views here.
#site products
def products(request):
    """
    Render the services page.
    """
    return render(request, 'products/products.html')

# site products details
def products_datail(request):
    """
    Render the services page.
    """
    return render(request, 'products/products_detail.html')