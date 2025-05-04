from django.urls import path
from .views import views
url_principal = 'productos/'

urlpatterns = [
    # path( url_principal+'crear', views.candidato_crear, name='candidato_crear'),
    path(url_principal+'', views.products, name='products'),
    path(url_principal+'detalle/', views.products_datail, name='products_detail'),
]