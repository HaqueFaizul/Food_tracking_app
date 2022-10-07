from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.loadBookForm),
    path('insert',views.createBook),
    path('show',views.showbook),
    path('email',views.emailHandling),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)