
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('',views.profile,name='profile'),
    path('user_detail/',views.user_detail,name='user_detail'),
    path('favourite/',views.favourite,name='favourite'),
    path('loginreg/',views.loginreg,name='loginreg'),
]
