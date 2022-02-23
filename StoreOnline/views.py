from cmath import log
from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from StoreOnline.forms import RegisterForm
from django.contrib.auth.models import User
import products
from products.models import Product


def index(request):
    products= Product.objects.all().order_by('title')
    context={
            'title' : 'Productos',
            'message' : 'Listado de productos',
            'products' : products,
    }
    return render(request, 'index.html',context)   
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvido {}'.format(user.username))
            return redirect('products:index')
        else:
            messages.error(request, 'Usuario o contraseña NO validos')
    return render(request, 'user/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada correctamente')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect(index)
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request,'Usuario creado de forma exitosa',)
            return redirect('products:index')
    context = {
        'form' : form,
    }
    return render(request, 'user/register.html', context)
