from django.shortcuts import render
from django.template.context_processors import request
from .models import Product, ProductCategory
from django.http import Http404
from django.shortcuts import get_object_or_404
from  django.db.models import Avg, Min

def product_list(request):
    products = Product.objects.all().order_by('title') # sort kardan barax - az ziyad -price
    #Product.objects.filter(category__url_field='mobile')
    nuumber_of_product = products.count()
    avg_rating = products.aggregate(Min("price"), Avg("price"))
    return render(request,  'product_module/product_list.html' , ({
        'products' : products,
        'total_number_of_products': nuumber_of_product,
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