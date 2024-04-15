from django.shortcuts import render
from django.template.context_processors import request
from .models import Product, ProductCategory
from django.http import Http404
from django.shortcuts import get_object_or_404
from  django.db.models import Avg, Min

def product_list(request):
    products = Product.objects.all().order_by('title')[:5] # sort kardan barax - az ziyad -price
    #[:5] 5 taye akhar
    return render(request,  'product_module/product_list.html' , ({
        'products' : products,
    }))

def product_detail(request, slug):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404
    product = get_object_or_404(Product, slug=slug) # = try except
    return render(request, 'product_module/product_details.html', {
        'product': product
    })