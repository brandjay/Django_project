from distutils.command.upload import upload
from django.db import models
from django.forms import CharField, ImageField

from django.contrib import admin


class profile(models.Model):

  profilepic = models.ImageField(upload_to='images/profilepics', null = True)

def __str__(self):
    return self.title

    
    #display the name of post in django admin