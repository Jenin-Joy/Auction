from django.shortcuts import render,redirect
from Guest.models import *
# Create your views here.

def artist(request):
    if request.method=="POST":
        tbl_artist.objects.create(
            artist_name=request.POST.get("name"),
            artist_Email=request.POST.get("mail"),
            artist_password=request.POST.get("pass")
        )
        return redirect("Guest:artist")
    else:
        return render(request, 'Guest/Artist.html')

def user(request):
    if request.method=="POST":
        tbl_user.objects.create(
            user_name=request.POST.get("name"),
            user_Email=request.POST.get("mail"),
            user_password=request.POST.get("pass")
        )
        return redirect("Guest:user")
    else:
        return render(request, 'Guest/User.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("txtemail")
        password = request.POST.get("pass")
        usercount = tbl_user.objects.filter(user_Email=email,user_password=password).count()
        artistcount = tbl_artist.objects.filter(artist_Email=email,artist_password=password).count()

        if usercount > 0:
            user = tbl_user.objects.get(user_Email=email,user_password=password)
            request.session["uid"] = user.id
            return redirect("User:viewauctionlist")
        
        elif artistcount > 0:
            artist = tbl_artist.objects.get(artist_Email=email,artist_password=password)
            request.session["aid"] = artist.id
            return redirect("Artist:addartwork")
        else:
            return render(request, 'Guest/Login.html',{"msg":"Invalid Email or Password"})
    else:
            return render(request, 'Guest/Login.html')