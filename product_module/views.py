from django.shortcuts import render
from django.template.context_processors import request
from .models import Product, ProductCategory
from django.http import Http404
from django.shortcuts import get_object_or_404
from  django.db.models import Avg, Min

def product_list(request):
    console = ProductCategory(title='play station', url_field='playstation')
    console.save()
    ps_4 = Product(title='play station 4', price=1500000000, category=console,short_description='this is fun', rating=5)
    ps_4.save()
    ps_3 = Product(title='play station 3', price=1200000000, category=console,short_description='this is old', rating=3)
    ps_3.save()

    mobile = ProductCategory(title='list of mobiles', url_field='mobile')
    mobile.save()
    iphone = Product(title='iphon mobile', price=20000000, category=mobile, short_description='this is goood', rating=5)
    iphone.save()

    products = Product.objects.all().order_by('title') # sort kardan barax - az ziyad -price
    nuumber_of_product = products.count()
    avg_rating = products.aggregate(Avg("rating"), Min("price"), Avg("price"))
    return render(request,  'product_module/product_list.html' , ({
        'products' : products,
        'total_number_of_products': nuumber_of_product,
        'average_rating': avg_rating
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