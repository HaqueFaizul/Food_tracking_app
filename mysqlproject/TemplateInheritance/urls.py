from django.urls import path
from .import views

urlpatterns=[
    path('loadPage',views.loadPage),
    path('', views.loadIndex)
]