from django.urls import path
from .import views

urlpatterns=[
    path('setc',views.SetCookie),
    path('getc',views.GetCookie),
    path('delc', views.DelCookie),
    path('sets', views.SetSession),
    path('gets', views.GetSession),
    path('dels', views.DelSession),
]