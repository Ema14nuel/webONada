from django.urls import path
from .views import views, productsView
# url_principal = 'sites/'

urlpatterns = [
    path('', views.home, name='inicio'),
    
]