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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price =product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or 1000000
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name =self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)
        if end_price is not None:
            query = query.filter(price__lte=end_price)
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
