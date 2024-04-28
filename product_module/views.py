from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductBrand


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price'] # moratab sazi az kamtarin gheymat
    paginate_by = 1 # show
    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name =self.kwargs.get('brand')
        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)
        if category_name is not None:
            query = query.filter(category__url_field__iexact=category_name)
        return query

class ProductDetaiView(DetailView):
    template_name = 'product_module/product_details.html'
    model = Product

def product_categoreis_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/component/product_categoreis_component.html', context)

def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context= {
        'brands' : product_brands
    }
    return render(request, 'product_module/component/product_brands_component.html', context)
