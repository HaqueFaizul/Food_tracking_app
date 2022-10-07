from django.urls import path
from .import views

urlpatterns=[
    path('',views.EmployeeShow.as_view()),
    path('emp/<int:eid>',views.EmployeeUpdateDelete.as_view())
]