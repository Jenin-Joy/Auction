from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime, timedelta , time, datetime
# Create your views here.

def viewauctionlist(request):
    auction = tbl_auctionhead.objects.all()
    # print(time(0, 0, 30))
    return render(request,"User/ViewAuctionList.html",{"auction":auction})

def auction(request, id):
    auction = tbl_auctionhead.objects.get(id=id)
    return render(request,"User/Auction.html",{"artwork":auction,"id":id})

def ajaxplacebid(request):
    # print(request.GET.get("amount"))
    if int(request.GET.get("amount")) > int(request.GET.get("amt")):
        getamount = tbl_auctionbody.objects.filter(auction=request.GET.get("auctionid")).last()
        if getamount:
            if int(getamount.auctionbody_amount) < int(request.GET.get("amount")):
                tbl_auctionbody.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),user=tbl_user.objects.get(id=request.session["uid"]),auctionbody_amount=request.GET.get("amount"))
                timer = tbl_timmer.objects.filter(auction=request.GET.get("auctionid")).count()
                if timer > 0:
                    t = tbl_timmer.objects.get(auction=request.GET.get("auctionid"))
                    t.timmer = time(0, 0, 30)  # Adds 30 seconds
                    t.save()
                else:
                    tbl_timmer.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),timmer=time(0, 0, 30))
                return JsonResponse({"msg":"Bid Placed Successfully","color":"rgb(94, 177, 97)"})
            else:
                return JsonResponse({"msg":"Please Enter Valid Amount","color":"red"})
        else:
            tbl_auctionbody.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),user=tbl_user.objects.get(id=request.session["uid"]),auctionbody_amount=request.GET.get("amount"))
            timer = tbl_timmer.objects.filter(auction=request.GET.get("auctionid")).count()
            if timer > 0:
                t = tbl_timmer.objects.get(auction=request.GET.get("auctionid"))
                t.timmer = time(0, 0, 30)  # Adds 30 seconds
                t.save()
            else:
                tbl_timmer.objects.create(auction=tbl_auctionhead.objects.get(id=request.GET.get("auctionid")),timmer=time(0, 0, 30))
            return JsonResponse({"msg":"Bid Placed Successfully","color":"rgb(94, 177, 97)"})
    else:
        return JsonResponse({"msg":"Please Enter Valid Amount","color":"red"})

def ajaxgetbid(request):
    auctionid = request.GET.get("auctionid")
    auctiondata = tbl_auctionbody.objects.filter(auction=auctionid).last()
    if auctiondata:
        return JsonResponse({"user":auctiondata.user.user_name,"amount":auctiondata.auctionbody_amount})
    else:
        return JsonResponse({"user":"","amount":0})

def ajaxclosebid(request):
    auctionid = request.GET.get("auctionid")
    auctiondata = tbl_auctionbody.objects.filter(auction=auctionid).last()
    # print(auctiondata.id)
    auctionbody = tbl_auctionbody.objects.get(id=auctiondata.id)
    auctionbody.auctionbody_status = 1
    auctionbody.save()
    auctionhead = tbl_auctionhead.objects.get(id=auctiondata.auction.id)
    auctionhead.auctionhead_status = 2 
    auctionhead.auction_totalamount = auctionbody.auctionbody_amount
    auctionhead.save()
    # time = tbl_timmer.objects.get(auction=auctionid)
    # time.timmer_status = 1
    # time.save()
    return JsonResponse({"msg":"Auction Completed...","user":auctiondata.user.user_name,"amount":auctiondata.auctionbody_amount})

def ajaxgettimmer(request):
    auction_id = request.GET.get("auctionid")
    userdata = tbl_auctionbody.objects.filter(auction=auction_id).last()

    if userdata is not None:
        userid = userdata.user.id
        if userid == request.session["uid"]:
            timmer_count = tbl_timmer.objects.filter(auction=auction_id, timmer_status=0).count()
            if timmer_count > 0:
                t = tbl_timmer.objects.get(auction=auction_id)
                if t.timmer > time(0, 0, 0):
                    # Convert time to datetime for subtraction
                    current_time = datetime.combine(datetime.today(), t.timmer)
                    new_time = (current_time - timedelta(seconds=1)).time()

                    # Update timer in database
                    t.timmer = new_time
                    t.save()

                    return JsonResponse({"time": t.timmer, "time_up": False})
                else:   
                    # Timer expired
                    return JsonResponse({"time": time(0, 0, 0), "time_up": True})
            else:
                return JsonResponse({"time": time(0, 0, 0), "time_up": True})
        else:
            timmer_count = tbl_timmer.objects.filter(auction=auction_id).count()
            if timmer_count > 0:
                ti = tbl_timmer.objects.filter(auction=auction_id).last()
                if ti.timmer > time(0, 0, 0):
                    return JsonResponse({"time": ti.timmer, "time_up": False})
                else:
                    return JsonResponse({"time": time(0, 0, 0), "time_up": True})
            else:
                return JsonResponse({"time": time(0, 0, 0), "time_up": True})
    else:
        return JsonResponse({"time": time(0, 0, 30), "time_up": False})

def myauction(request):
    auction = tbl_auctionbody.objects.filter(user=request.session["uid"],auctionbody_status=1)
    return render(request,"User/MyAuction.html",{'auction':auction})

def auctionpayment(request, id):
    auction = tbl_auctionbody.objects.get(id=id)
    amount = auction.auctionbody_amount
    auc = tbl_auctionhead.objects.get(id=auction.auction.id)
    if request.method == "POST":
        auc.auctionhead_status = 3
        auc.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":amount})

def loader(request):
    return render(request, 'User/Loader.html')

def paymentsuc(request):
    return render(request, 'User/Payment_suc.html')