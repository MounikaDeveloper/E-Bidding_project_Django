from django.db import models

class RegisterModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    doj = models.DateField(auto_now_add=True)

class ProductModel1(models.Model):
    pno=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=30)
    bidprice=models.FloatField()
    information=models.TextField()
    image=models.ImageField(upload_to="productmodel")
    status=models.CharField(max_length=30)
    sellerinfo=models.ForeignKey(RegisterModel,on_delete=models.CASCADE)


