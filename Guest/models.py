from django.db import models

# Create your models here.

class tbl_artist(models.Model):
    artist_name=models.CharField(max_length=50)
    artist_Email=models.CharField(max_length=50)
    artist_password=models.CharField(max_length=50)

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_Email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)