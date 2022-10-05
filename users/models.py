from distutils.command.upload import upload
from django.db import models
from django.forms import CharField, ImageField
from django.forms.fields import DateTimeField
from matplotlib import image
from sqlalchemy import true
from django.contrib import admin
from django.conf import settings # needed for importing author function
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
        
    # include title 
    title = models.CharField(null=True, max_length=50)
    
#needs to be made optional blank = True must change jina loging to if single_post_img then post else skip
    image = models.ImageField(upload_to='images/', null = True) 

    quote = HTMLField(null=True) #was models.Textfield

    date = models.DateTimeField(auto_now_add=True, null=True)
   

