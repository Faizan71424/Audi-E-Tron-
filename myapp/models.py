from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=22)
    blog= models.CharField(max_length=1000)