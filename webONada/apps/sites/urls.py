from django.urls import path
from .views import views
# url_principal = 'sites/'

urlpatterns = [
    path('', views.home, name='inicio'),
    path('nosotros/', views.about, name='about'),
    
]