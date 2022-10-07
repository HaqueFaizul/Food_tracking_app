from django .urls import path
from .import views

urlpatterns=[
    path('loadform',views.loadform),
    path('display',views.displayform),
    path('',views.loadStudentForm),
    path('insert',views.insertStudent),
    path('show',views.displayStudent),
    path('delete/<int:sid>',views.deleteStudent, name='delete'),
    path('edit/<int:sid>',views.editStudent, name='edit'),
    path('update/<int:sid>',views.updateStudent),
    path('stdstatus/<int:sid>/<str:status>',views.studentstatus,name='stdstatus'),
]