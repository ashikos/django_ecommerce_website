from django.db import models
from .category import Category
from .color import Color


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Color = models.ForeignKey(Color, on_delete=models.CASCADE, default='',
                              null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    img = models.ImageField(upload_to='products')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(categoryid):
        return Product.objects.filter(Category=categoryid)

    @staticmethod
    def get_all_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
