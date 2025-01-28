from django.shortcuts import render

#models
from apps.products.models import ProductPresentation


# Create your views here.
def products_list(request):
    products_list  = ProductPresentation.objects.select_related('product').filter(active=True)
    

    context = {
        'products_list': products_list
        }
    return render(request, 'site/products.html', context)