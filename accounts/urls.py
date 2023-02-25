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
    path('password_reset/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
     ]