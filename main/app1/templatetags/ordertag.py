from unicodedata import name
from django import template

#from main.app1.views import cart


register = template.Library()

      
@register.filter(name='multiply')
def multiply(price,quantity):
    return price * quantity
                 
