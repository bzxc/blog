from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    #文章种类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Label(models.Model):
    #文章标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artical(models.Model):
    #文章表
    title = models.CharField(max_length=100) #标题
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.ManyToManyField(Label, blank=True)
    creat_time = models.DateTimeField() #创建时间
    modify_time = models.DateTimeField() #修改时间
    author = models.ForeignKey(User, on_delete=models.CASCADE) #作者
    body = models.TextField()

    def __str__(self):
        return self.title




