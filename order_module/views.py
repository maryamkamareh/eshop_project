from django.shortcuts import render, redirect
from django.views.generic import CreateView

from product_module.models import Product
from .models import Order, OrderDetail
# Create your views here.

# class AddToOrderView(CreateView):
#     template_name = 'order_module/orders.html'
#     form_class = Order
#     success_url = '/order/'

def add_to_order(request, product_id):
    product = Product.objects.get(id=product_id)
    print(Order.objects.get_or_create(user=request.user))
    order = Order.objects.get_or_create(user=request.user)
    order_detail= OrderDetail.objects.get_or_create(order=order, product=product)
    order_detail.quantity += 1
    order_detail.save()
    return redirect('product-list')

def order(request):
    products = Product.objects.all()
    order = Order.objects.get(user=request.user)
    order_detail = OrderDetail.objects.filter(order=order)
    total_price = sum(item.product.price * item.quantity for item in order_detail)
    return render(request, 'order_module/orders.html', {'order_detail': order_detail, 'total_price': total_price, 'product': products})