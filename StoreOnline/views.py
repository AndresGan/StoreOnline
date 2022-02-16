from cmath import log
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login


def index(request):
    context={
        'title': 'Productos',
        'message': 'Listado de productos',
        'products': [
            {'title': 'Playera','price':20000,'stock':True},
            {'title': 'Camisa','price':40000,'stock':True},
            {'title': 'Mochila','price':30000,'stock':False},
        ]
    }
    return render(request, 'index.html',context)
    
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print("Usted me esta autenticando")
        else:
            print("usted es como pirata")
    return render(request, 'user/login.html', {})