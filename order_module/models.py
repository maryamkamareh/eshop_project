from django.db import models
from product_module.models import Product
# Create your models here.
class Order(models.Model):
    user = models.CharField(null=True, max_length=300, verbose_name='کاربر')
    is_paid = models.BooleanField(null=True, verbose_name='نهایی شده/نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = ' سبدهای خرید کاربران'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')
    def __str__(self):
        return str(self.order)
    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural ='لیست جزییات سبدهای خرید'
