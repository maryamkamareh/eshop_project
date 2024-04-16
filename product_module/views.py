from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Product, ProductCategory
from django.http import Http404
from django.shortcuts import get_object_or_404
from  django.db.models import Avg, Min

# def product_list(request):
#     products = Product.objects.all().order_by('title')[:5] # sort kardan barax - az ziyad -price
#     #[:5] 5 taye akhar
#     return render(request,  'product_module/product_list.html' , ({
#         'products' : products,
#     }))
class ProductListView(TemplateView):
    template_name = 'product_module/product_list.html'
    def get_context_data(self, **kwargs):
        products = Product.objects.all().order_by('title')[:5]
        contex = super(ProductListView, self).get_context_data()
        contex['products'] = products
        return contex
# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug) # = try except
#     return render(request, 'product_module/product_details.html', {
#         'product': product
#     })

class ProductDetaiView(TemplateView):
    template_name = 'product_module/product_details.html'
    def get_context_data(self, **kwargs):
        slug = kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        contex = super(ProductDetaiView, self).get_context_data()
        contex['product'] = product
        return contex