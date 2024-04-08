from django.shortcuts import render
from django.template.context_processors import request
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request,  'product_module/product_list.html' , ({
        'products' : products
    }))
