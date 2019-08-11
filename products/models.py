from django.db import models
import datetime

class Product(models.Model):
    pid=models.AutoField(primary_key=True,unique=True)
    title=models.CharField(max_length=255)
    price_on_amazon=models.CharField(max_length=50)
    image=models.TextField()
    mrp=models.CharField(max_length=50)
    saving=models.CharField(max_length=50)
    amazon_url=models.TextField(max_length=100)
    pub_date=models.DateTimeField()
    other_images=models.TextField()
    android=models.CharField(max_length=32)
    ram=models.CharField(max_length=32)
    weight=models.CharField(max_length=32)
    battery=models.CharField(max_length=32)
    display=models.CharField(max_length=255)
    flipkart_url=models.CharField(max_length=255)
    price_on_flipkart=models.CharField(max_length=255)




class Posts(models.Model):
    title=models.CharField(max_length=255)
    price=models.CharField(max_length=50)
    image=models.TextField()
