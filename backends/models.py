from django.db import models

# Create your models here.



class Test(models.Model):
    name = models.CharField(max_length=100)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    msg = models.TextField(null=True)



class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ManyToManyField("Author")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.DateField()
    def __str__(self):
        return self.name