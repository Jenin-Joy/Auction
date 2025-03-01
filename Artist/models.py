from django.db import models
from Guest.models import *
# Create your models here.

class tbl_artwork(models.Model):
        artwork_photo = models.FileField(upload_to='Assets/User/Photo/')
        artwork_status = models.IntegerField(default=0)
        artwork_price = models.CharField(max_length=30)
        artwork_description = models.CharField(max_length=50)
        artist = models.ForeignKey(tbl_artist, on_delete=models.CASCADE)

class tbl_auctionhead(models.Model):
        artwork = models.ForeignKey(tbl_artwork, on_delete=models.CASCADE)
        auctionhead_amount = models.CharField(max_length=30)
        auctionhead_date = models.DateField(auto_now_add=True)
        auctionhead_todate = models.DateField()
        auction_starttime = models.CharField(max_length=30)
        auctionhead_status = models.IntegerField(default=0)
        auction_totalamount = models.CharField(max_length=30)