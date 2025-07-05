from django.urls import path
from apps.users.views import loginView
url_principal = 'users/'

urlpatterns = [
    path('login', loginView.login, name='login'),
    path( url_principal+'register', loginView.register, name='register'),
    path( url_principal+'recovery', loginView.recovery, name='recovery'),
    # path( url_principal+'login', loginView.login, name='access'),
]