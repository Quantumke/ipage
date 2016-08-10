from django.db import models

# Create your models here.

class contactus(models.Model):
    name=models.CharField(unique=False, max_length=100)
    email=models.CharField(unique=False, max_length=100)
    phone=models.CharField(unique=False, max_length=100)
    message=models.TextField(unique=False, max_length=500)

    def __unicode__(self):
        return  self.name

class prospects(models.Model):
    name=models.CharField(max_length=100, unique=False)
    email=models.CharField(max_length=100, unique=False)
    phone=models.CharField(max_length=100, unique=False)
    package=models.CharField(max_length=100, unique=False)
    description=models.CharField(max_length=100, unique=False)

    def __unicode__(self):
        return self.name

