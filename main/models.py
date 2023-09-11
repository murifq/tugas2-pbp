from django.db import models

# Create your models here.
class Item(models.Model):
  photo_url = models.CharField(max_length=512, default="https://static.vecteezy.com/system/resources/previews/005/337/799/original/icon-image-not-found-free-vector.jpg")
  name = models.CharField(max_length=255)
  amount =  models.IntegerField(default=0)
  price =  models.IntegerField(default=0)
  description = models.TextField()
  rating =  models.IntegerField(default=0)
  sold =  models.IntegerField(default=0)