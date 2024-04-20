from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        if category_name is not None:
            query = query.filter(category__url__title__iexact=category_name)
        return query

class ProductDetaiView(DetailView):
    template_name = 'product_module/product_details.html'
    model = Product

def product_categoreis_component(request: HttpRequest):
    product_categories = ProductCategory.objects.all()
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/component/product_categoreis_component.html', context)