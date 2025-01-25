from django.urls import path
from .views import views
# url_principal = 'sites/'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home', views.home, name='home'),
    path('productos', views.products_list, name='products'),
]