from django.urls import path
from .views import views
url_principal = 'productos/'

urlpatterns = [
    # path( url_principal+'crear', views.candidato_crear, name='candidato_crear'),
    path(url_principal+'', views.products, name='products'),
    path(url_principal+'detalle/<int:pk>', views.products_detail, name='products_detail'),
    path(url_principal+'categorias/', views.categories, name='categories'),
    path(url_principal+'categorias/detalle/<int:pk>', views.categories_detail, name='categories_detail'),

]