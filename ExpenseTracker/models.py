from django.db import models
from django.contrib.auth.models import User
    

class Exp(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="display")
    des=models.CharField(max_length=100)
    amt=models.IntegerField()
    date=models.CharField(max_length=100)
    pay=models.CharField(max_length=100)
   # user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="display")

def __str__(self):
    return self.name
    











#class Pen(models.Model):
 #   des=models.CharField(max_length=100)
  #  amt=models.IntegerField()
   # date=models.CharField(max_length=100)
    #pay=models.CharField(max_length=100)





