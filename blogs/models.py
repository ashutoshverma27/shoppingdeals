from django.db import models

class BlogPost(models.Model):
    postid=models.AutoField(primary_key=True,unique=True)
    title=models.CharField(max_length=255)
    post=models.TextField()
    url=models.CharField(max_length=255,blank=True)
    date=models.DateTimeField()
    image=models.TextField()
