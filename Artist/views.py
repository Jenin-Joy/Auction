from django.shortcuts import render,redirect
from User.models import *
from Artist.models import *
# Create your views here.

def addartwork(request):
    artwork = tbl_artwork.objects.filter(artist_id=request.session['aid'])
    if request.method == "POST":
        tbl_artwork.objects.create(artwork_photo=request.FILES.get("txtphoto"),
        artwork_price=request.POST.get("txtprice"),
        artwork_description=request.POST.get("txtdescription"),
        artist=tbl_artist.objects.get(id=request.session['aid']))

        return redirect("Artist:addartwork")
    else:
        return render(request, 'Artist/AddArtwork.html',{"artwork":artwork})

def addtoauction(request,id):
   artwork = tbl_artwork.objects.get(id=id) 
   if request.method == "POST":
    auctioncount = tbl_auctionhead.objects.filter(artwork=artwork).count()
    if auctioncount > 0:
        return render(request,"Artist/AddToAuction.html",{"msg":"This Product Already Added To Auction Thank You..!!","id":id})
    else:
        tbl_auctionhead.objects.create(artwork=artwork,
                                        auctionhead_amount=request.POST.get('txt_amount'),
                                        auctionhead_todate=request.POST.get('txt_todate'),
                                        auction_starttime=request.POST.get('txt_starttime'))
        artwork.artwork_status = 2
        artwork.save()
        return render(request,"Artist/AddToAuction.html",{"msg":"Product Added To Auction List","id":id})
   return render(request,"Artist/AddToAuction.html",{"data":artwork})

def auctionlist(request):
    auction = tbl_auctionhead.objects.filter(artwork__artist=request.session["aid"],auctionhead_status__lt=3)
    return render(request,"Artist/AuctionList.html",{"auction":auction})

def auctionupdation(request, id, status):
    auction = tbl_auctionhead.objects.get(id=id)
    auction.auctionhead_status = status
    auction.save()
    return redirect('Artist:auctionlist')

def completedauction(request):
    auction = tbl_auctionhead.objects.filter(artwork__artist=request.session["aid"],auctionhead_status__gt=2)
    for i in auction:
        aucbody = tbl_auctionbody.objects.get(auction=i.id, auctionbody_status=1)
        i.user = aucbody.user.user_name
    return render(request,"Artist/CompletedAuction.html",{"auction":auction})