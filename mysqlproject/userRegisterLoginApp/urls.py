from django.urls import path
from .import views

urlpatterns=[
    path('',views.Home),
    path('signup',views.loadSignUp, name='signup'),
    path('signin',views.loadSignIn, name='signin'),
    path('loadigninprofile',views.loadUserSignIn),
    path('usersignup',views.signup),
    path('usersignin',views.usersignin),
    path('usersignout', views.userlogout, name='usersignout'),

]