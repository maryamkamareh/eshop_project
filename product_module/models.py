from django.db import models
from django.urls import reverse

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_field = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده/ حذف نشده')
    def __str__(self):
        return f"{self.title}-{self.url_field}"
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural= 'دسته بندی ها'

class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True,  verbose_name='نام برند')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(
        ProductCategory,
        related_name='product_categories',
        verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', null=True, verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE,blank=True, null=True, verbose_name='برند')
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=350,db_index=True, blank=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(db_index=True,verbose_name= 'توضیحات اصلی')
    is_active = models.BooleanField(default=False, verbose_name='فعال/ غیرفعال')
    slug = models.SlugField(default="", null=False, blank=True, max_length=200, unique=True, verbose_name='عنوان در url') #DB INDEX sorat va amalkarde behtar
    is_delete = models.BooleanField(verbose_name='حذف شده/ حذف نشده')

    def get_absolute_url(self):
        return reverse('product-detail',args=[self.slug])

    def save(self, *args, **kwargs): # overwrite save
        #self.slug = slugify(self.title) # samsung galaxy s 20 +> samsung-galexy-s-20
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural= 'محصولات'

class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='title')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')
    def __str__(self):
        return self.caption
    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصول'