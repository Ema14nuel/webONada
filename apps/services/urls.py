from django.urls import path
from .views import views
url_principal = 'servicios/'

urlpatterns = [
    # path( url_principal+'crear', views.candidato_crear, name='candidato_crear'),
    path(url_principal+'', views.services, name='services'),
]