
from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    
    
    
    @staticmethod
    
    def get_customer_by_username(username) :
        try:
            if Customer.objects.get(username=username):
                return Customer.objects.get(username=username)
        except:
            return None
    
    @staticmethod    
    def get_all_customer_by_id(id) :
        return Customer.objects.filter(id=id)
 