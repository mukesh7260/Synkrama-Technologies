from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=25,null=True,blank=True) 
    body = models.TextField(null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True) 
    
    def __str__(self):
            return self.title
    

# write own models 

class Mobile(models.Model): 
    names = models.CharField(max_length=25,null=True,blank=True) 
    rams = models.IntegerField(null=True,blank=True) 
    roms = models.IntegerField(null=True,blank=True) 
    prices = models.IntegerField(null=True,blank=True) 
    brands = models.CharField(max_length=25,null=True,blank=True) 
    
    def __str__(self):
            return self.name