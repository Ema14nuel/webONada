from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

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