from django.shortcuts import render # type: ignore

#models
from apps.products.models import ProductPresentation

#form
from apps.sites.forms.formFilter import formFilterProduct


# Create your views here.
def products_list(request):

    print("GET Data:", request.GET)
    products_list = ProductPresentation.objects.select_related('product', 'product__category').prefetch_related('product__images', 'product__tags').filter(active=True)

    form = formFilterProduct(request.GET if request.GET else None)

    if form.is_valid():
        
        print('Formulario validado')
        
        if form.cleaned_data.get('featured_title'):
            products_list = products_list.filter(featured_title__icontains=form.cleaned_data['featured_title'])
        
        # if form.cleaned_data.get('category'):
        #     categories = form.cleaned_data['category']
        #     print('Categorías seleccionadas:', categories)
        #     products_list = products_list.filter(product__category__in=categories)
        # if form.cleaned_data.get('price_min'):
        #     products_list = products_list.filter(price__gte=form.cleaned_data['price_min'])
        # if form.cleaned_data.get('price_max'):
        #     products_list = products_list.filter(price__lte=form.cleaned_data['price_max'])
    else:
        print("Errores en el formulario:", form.errors.as_data()) 

        products_list = ProductPresentation.objects.select_related('product', 'product__category').prefetch_related('product__images', 'product__tags').filter(active=True)


    context = {
        'products_list': products_list,
        'form': form
    }

    return render(request, 'site/products.html', context)

def home(request):
    
    return render(request, 'index.html')