from django.urls import path
from Artist import views
app_name = "Artist"
urlpatterns = [
    path('addartwork/', views.addartwork , name='addartwork'),
    path('addtoauction/<int:id>', views.addtoauction , name='addtoauction'),
    path('auctionlist/', views.auctionlist , name='auctionlist'),
    path('auctionupdation/<int:id>/<int:status>', views.auctionupdation , name='auctionupdation'),
    path('completedauction/', views.completedauction , name='completedauction'),
]