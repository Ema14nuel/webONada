from django.shortcuts import render

#models
from apps.products.models import ProductPresentation

#form
from apps.sites.forms.formFilter import formFilterProduct


# Create your views here.
def products_list(request):

    products_list  = ProductPresentation.objects.select_related('product').filter(active=True)
    form = formFilterProduct(request.GET or None)

    print(products_list)

    context = {
        'products_list': products_list,
        'form': form
        }
    return render(request, 'site/products.html', context)