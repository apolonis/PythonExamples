from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)


    def __init__(self,name,lastname,image_url):
        self.name = name
        self.lastname = lastname
        self.image_url = image_url

