from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    day=models.CharField(max_length=50,default='something')
    name=models.CharField(max_length=50,default='spmething')
    description=models.CharField(max_length=100,default='something')