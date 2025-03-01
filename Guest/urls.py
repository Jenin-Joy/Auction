from django.urls import path
from Guest import views
app_name = "Guest"
urlpatterns = [
    path('artist/', views.artist , name='artist'),
    path('user/', views.user , name='user'),
    path('', views.login , name='login'),
]