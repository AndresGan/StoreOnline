from itertools import product
from pyexpat import model
from re import template
from django.shortcuts import render
from operator import imod
from django.views import generic
from products.models import Product
from django.shortcuts import render

class ProductListView(generic.ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('title')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado Productos'
        context['products'] = context['object_list']
        return context
    
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product.html'