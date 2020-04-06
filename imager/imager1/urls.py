from django.urls import path
from . import views

urlpatterns=[
    path('imager', views.home, name='base'),
    path('imager/upload/', views.upload, name='upload'),
    path('imager/upload/add', views.add, name='add'),
] 