from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=220)
    token = models.CharField(max_length=220)
    headImg = models.CharField(max_length=100)


class article(models.Model):
    title = models.CharField(max_length=40)
    create_time = models.CharField(max_length=50)
    author = models.CharField(max_length=40)
    content = models.TextField()