from django.http import HttpRequest, JsonResponse

from product_module.models import Product
from .models import Order, OrderDetail


def add_product_to_order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')
    if count < 1:
        return JsonResponse({
            'status': 'invalid_count'
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر به سبد خرید اضافه شد',
                'condirm_button_text': 'باشه ممنونم'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'condirm_button_text': 'مرسییییی'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'اول وارد شوید',
            'condirm_button_text' : 'باشههه'
    })
