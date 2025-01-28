from django.urls import path
from .views import views, productsView
# url_principal = 'sites/'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home', views.home, name='home'),
    path('productos', productsView.products_list, name='products'),
]