from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

def login(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    #     if request.method == 'POST':
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('home')
    #         else:
    #             messages.error(request, 'Invalid username or password')
    
    context = {
        'title': 'Iniciar sesión',
    }

    return render(request, './users/login.html', context)

def register(request):
    context = {
        'title': 'Registrarse',
    }

    return render(request, './users/register.html', context)

def recovery(request):
    context = {
        'title': 'Recuperar contraseña',
    }

    return render(request, './users/recovery.html', context)