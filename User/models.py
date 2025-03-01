from django.db import models
from Artist.models import *
# Create your models here.

class tbl_auctionbody(models.Model):
    auctionbody_amount = models.CharField(max_length=30)
    auction = models.ForeignKey(tbl_auctionhead, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    auctionbody_status = models.IntegerField(default=0)

class tbl_timmer(models.Model):
    timmer = models.TimeField()
    auction = models.ForeignKey(tbl_auctionhead, on_delete=models.CASCADE)
    timmer_status = models.IntegerField(default=0)