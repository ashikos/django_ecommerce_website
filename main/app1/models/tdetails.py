from django.db import models

class Train_det(models.Model):
    name=models.CharField(max_length=50)
    bording=models.CharField(max_length=40)
    ending=models.CharField(max_length=50)    
    price=models.IntegerField()