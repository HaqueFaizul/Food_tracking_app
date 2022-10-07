from django.urls import path
from .import views

urlpatterns=[
    path('',views.loadIndex),
    path('getState',views.getState)
]