from django.urls import path
from .import views

urlpatterns=[
    path('',views.loadStudent),
    path('insert',views.insertStudent),
    path('display',views.displayStudent),
    path('destroy/<int:sid>',views.destroyStudent,name="destroy"),
    path('editstd/<int:sid>',views.EditStudent,name='editstd'),
]