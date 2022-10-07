from django .urls import path
from .import views

urlpatterns=[
    path('',views.HomePage),
    path('registration',views.LoadRegister,name='registration'),
    path('loadlogin',views.Loadlogin,name='login'),
    path('userprofile',views.Loaduserprofile),
    path('register',views.register),
    path('userlogin',views.userlogin),
    path('userlogout',views.userlogout,name='userlogout'),
]