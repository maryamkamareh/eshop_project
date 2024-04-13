from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.template.defaultfilters import title
from django.urls import reverse
from django.utils.text import slugify
class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_field = models.CharField(max_length=300, verbose_name='عنوان در url')
    def __str__(self):
        return f"{self.title}-{self.url_field}"
class ProductInformation(models.Model):
    color = models.CharField(max_length=200, verbose_name='color')
    size = models.CharField(max_length=200, verbose_name='size')
    def __str__(self):
        return f"{self.color} -{self.size}"
class Product(models.Model):
    title = models.CharField(max_length=300)
    product_information = models.OneToOneField('ProductInformation', on_delete=models.CASCADE,
                                               related_name='product_information', verbose_name='informations',
                                               null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)] , default=0)
    short_description = models.CharField(max_length=350, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True) #DB INDEX sorat va amalkarde behtar
    def get_absolute_url(self):
        return reverse('product-detail',args=[self.slug])

    def save(self, *args, **kwargs): # overwrite save
        self.slug = slugify(self.title) # samsung galaxy s 20 +> samsung-galexy-s-20
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"
