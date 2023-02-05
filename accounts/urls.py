from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('index', views.index,name="index"),
    path('studentlogin', views.studentlogin,name="studentlogin"),
    path('studentregister', views.studentregister,name="studentregister") ,
    path('logout',views.logout,name="logout"),
     ]