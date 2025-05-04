from django.urls import path
from .views import views
# url_principal = 'sites/'

urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros/', views.about, name='about'),
    path('contacto/', views.contact, name='contact'),
    
]