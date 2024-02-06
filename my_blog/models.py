from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,default=None)
    content = models.TextField(default=None)
    image = models.ImageField(default=None)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    create_date =models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(default=None,blank=True,null=True)
    content = models.TextField(default=None)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=datetime.now)
    