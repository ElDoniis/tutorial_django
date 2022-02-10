from distutils.command.upload import upload
from nturl2path import url2pathname
from django.db import models
from matplotlib import image
from matplotlib.pyplot import title

# Create your models here.

class Movie(models.Model):
    title =  models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True) 