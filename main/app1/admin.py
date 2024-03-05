from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

from .models.color import Color
from .models.chechout import Checkout


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'Category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminColor(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'phone']


class AdminCheckout(admin.ModelAdmin):
    list_display = ['product', 'customer', 'price', 'quantity', 'date',
                    'status']

# Register your models here.


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Color, AdminColor)
admin.site.register(Checkout, AdminCheckout)
