from django.db import models


# Create your models here.

class Service(models.Model):
    nomi = models.CharField(max_length=50)
    text = models.TextField()
    rasm = models.ImageField(upload_to='media')
    date = models.DateField(auto_now=True)


class Worker(models.Model):
    ism = models.CharField(max_length=50)
    lavozim = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Project(models.Model):
    nomi = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    nomi = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    nomi = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Messages(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
