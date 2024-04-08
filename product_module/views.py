from django.shortcuts import render
from django.template.context_processors import request
from .models import Product
from django.http import Http404
from django.shortcuts import get_object_or_404


def product_list(request):
    products = Product.objects.all()
    return render(request,  'product_module/product_list.html' , ({
        'products' : products
    }))
def product_detail(request, slug):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404
    product = get_object_or_404(Product, slug=slug) # = try except
    return render(request, 'product_module/product_details.html', {
        'product' : product
    })