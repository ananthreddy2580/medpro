from django.db import models

class product(models.Model):
    pid=models.AutoField
    pname=models.CharField(max_length=30)
    pquantity=models.CharField(max_length=5)
    pprice=models.CharField(max_length=10)
    ptype=models.CharField(max_length=10)
    pdate=models.DateField(auto_now_add=True)



class product_details(models.Model):
    pname = models.CharField(max_length=30)
    pquantity = models.IntegerField()
    pcdate = models.DateField(auto_now_add=True)
    pudate = models.DateField(auto_now_add=True)

