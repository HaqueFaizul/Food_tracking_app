from django.urls import path
from .import views
urlpatterns=[
    path('',views.loadRegister, name='register'),
    path('loadlogin', views.loadLogin,name='loadlogin'),
    path('register',views.register),
    path('userlogin',views.userlogin),
    path('userlogout',views.logout, name='userlogout'),
]