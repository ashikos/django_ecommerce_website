from unicodedata import name
from django import template

#from main.app1.views import cart


register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    
    for id in keys:
        if int(id)==product.id:
            
            return True
    else:
        return False

@register.filter(name='cart_count')
def cart_count(product,cart):
    keys=cart.keys()
    
    for id in keys:
        if int(id)==product.id:
            
            return cart.get(id)
    else:
        return 0

@register.filter(name='product_total')
def product_total(product,cart):
    return product.price * cart_count(product,cart)


@register.filter(name='total_price')
def total_price(products,cart):
    sum=0
    for p in products:
        sum+=product_total(p,cart)
    return sum    

@register.filter(name='multiply')
def multiply(price,quantity):
    return price * quantity

