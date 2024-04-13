from django.contrib import admin
from . import models
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
admin.site.register(models.Product, ProductAdmin)