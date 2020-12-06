from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

class Post(models.Model):
    email = models.EmailField()
    text = models.TextField(max_length=4000)
    id = models.AutoField(primary_key=True)