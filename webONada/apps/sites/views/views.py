from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'site/home.html')

def inicio(request):
    return render(request, 'site/index.html')

def products_list(request):
    return render(request, 'site/products.html')