from django.urls import path
from User import views
app_name = "User"
urlpatterns = [
    path('viewauctionlist/',views.viewauctionlist,name="viewauctionlist"),
    path('auction/<int:id>',views.auction,name="auction"),
    path('ajaxplacebid/',views.ajaxplacebid,name="ajaxplacebid"),
    path('ajaxgetbid/',views.ajaxgetbid,name="ajaxgetbid"),
    path('ajaxclosebid/',views.ajaxclosebid,name="ajaxclosebid"),
    path('ajaxgettimmer/',views.ajaxgettimmer,name="ajaxgettimmer"),

    path('myauction/',views.myauction,name="myauction"),
    path('auctionpayment/<int:id>',views.auctionpayment,name="auctionpayment"),
    path('loader/',views.loader,name="loader"),
    path('paymentsuc/',views.paymentsuc,name="paymentsuc"),

]