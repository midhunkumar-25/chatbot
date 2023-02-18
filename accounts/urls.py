from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('index', views.index,name="index"),
    path('login', views.loginMethod,name="login"),
    path('register', views.registerMethod,name="register") ,
    path('logout',views.logoutMethod,name="logout"),
    path('chat',views.chatbotPage,name="chatbotPage"),
    path('chatquery',views.chatbotquery,name="chatbotquery"),
     ]