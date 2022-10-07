from django.urls import path
from .import views
urlpatterns=[
    path('',views.Home,name='myhome'),
    path('display',views.About,name='about'),
    path('show',views.ShowData),
    path('form',views.loadPerson)
]