from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30,unique=True)
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Seller(models.Model):
    sellerid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class ProductSeller(models.Model):
    selling_productid = models.AutoField(primary_key=True)
    sellerid = models.PositiveIntegerField(ForeignKey(Seller, on_delete=models.CASCADE))
    productid = models.PositiveIntegerField(ForeignKey(Product, on_delete=models.CASCADE))
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    
    def __str__(self):
        return self.selling_productid

class Address(models.Model):
    addressid = models.AutoField(primary_key=True)
    userid = models.PositiveIntegerField(ForeignKey(User, on_delete=models.CASCADE))
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.address

class Order(models.Model):
    orderid = models.AutoField(primary_key=True,unique=True)
    userid = models.PositiveIntegerField(ForeignKey(User, on_delete=models.CASCADE))
    selling_productid = models.PositiveBigIntegerField(ForeignKey(ProductSeller, on_delete=models.CASCADE))
    quantity = models.PositiveIntegerField()
    addressid = models.PositiveIntegerField(ForeignKey(Address, on_delete=models.CASCADE))
    sellerid = models.PositiveIntegerField(ForeignKey(Seller, on_delete=models.CASCADE))
    selling_productid = models.PositiveBigIntegerField(ForeignKey(ProductSeller, on_delete=models.CASCADE))
    total = models.PositiveIntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.orderid

