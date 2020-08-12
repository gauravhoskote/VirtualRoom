from django.db import models

# Create your models here.



class User(models.Model):
    dateofbirth = models.DateField(null=True)
    password = models.CharField(max_length=10)
    uniqueid = models.CharField(max_length=40, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, unique=True)



class Group(models.Model):
    adminuserid = models.CharField(max_length=40)
    uniqueid = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    liste = models.CharField(max_length=100)

