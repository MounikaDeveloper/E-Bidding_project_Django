from django.db import models

class RegisterModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    doj = models.DateField(auto_now_add=True)

class ProductModel(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    bprice = models.FloatField()
    info = models.TextField()
    image = models.ImageField(upload_to="products/")
    status = models.CharField(max_length=30)
    user = models.ForeignKey(RegisterModel,on_delete=models.CASCADE)

class BidTableModel(models.Model):
    bid = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    user_id = models.ForeignKey(RegisterModel,on_delete=models.CASCADE)
    amount = models.FloatField()
    bdate = models.DateField(auto_now_add=True)
    btime = models.TimeField(auto_now_add=True)