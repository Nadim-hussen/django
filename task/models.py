# from distutils.command.upload import upload
# from email.mime import image
# import imp
# from pickle import NONE
from tkinter import Y
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime
import os
# Create your models here.
def filepath(request,fileName):
    oldfileName= fileName
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    fileName = '%s%s',(timeNow,oldfileName)
    return os.path.join('upload/',fileName)

class upload_post(models.Model):
    name=models.TextField(max_length=191, null=False)
    price=models.TextField(max_length=50,null=False)
    description=models.TextField(max_length=500,null=True)
    # image = models.ImageField(upload_to=filepath,height_field=None,width_field=None, max_length=None)
    image = models.ImageField(upload_to=filepath,null=True,blank=True)

class Item(models.Model):
    name=models.TextField(max_length=191, null=False)
    # image = models.ImageField(upload_to=filepath,height_field=None,width_field=None, max_length=None)
    image = models.FileField(upload_to='task/',null=True,blank=True)