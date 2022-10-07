from django.urls import path
from .import views

urlpatterns=[
    path('',views.Store, name='store'),
    #path('/search', views.Search, name='search'),
    path('category/<slug:category_slug>', views.Store, name='category_product'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product_details, name='product_details'),
    path('search', views.Search, name='search'),

    #path('/<str:emp_name>',views.Store, name='category_product')
]