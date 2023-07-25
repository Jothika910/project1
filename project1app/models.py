from django.db import models

# Create your models
class signuptable(models.Model):
   username=models.CharField(max_length=256)
   password=models.IntegerField()
   email=models.EmailField()
   mobilenumber=models.BigIntegerField()
   firstname=models.CharField(max_length=256)
   lastname=models.CharField(max_length=256)
class detailstable(models.Model):
   username=models.CharField(max_length=250)
   login_time=models.CharField(max_length=250)
   logout_time=models.CharField(max_length=256)
   status=models.IntegerField()
class salarytable(models.Model):
      username = models.CharField(max_length=256)
      password = models.IntegerField()
      salary = models.IntegerField()
      status = models.CharField(max_length=256)
      date = models.DateTimeField()