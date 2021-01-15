from django.shortcuts import render
from django.views.generic import ListView
from core.almacen.models import Product
# Create your views here.
class ProductListView(ListView):
    model=Product
    template_name='list.html'