from operator import imod
from django.db import models
from .customer import Customer
from .product import Product
import datetime


class Checkout(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(blank=True, default='')
    phone = models.CharField(max_length=15, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
