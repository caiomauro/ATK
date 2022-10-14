from django.db import models
from django.contrib import admin


# Create your models here.

class userInfo(models.Model):
    password = models.CharField(max_length=20, default="", unique=True)
    username = models.CharField(max_length=12, unique=True)
    user_can_edit = models.BooleanField(null=False, default=False)

