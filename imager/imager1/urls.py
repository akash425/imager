from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='base'),
    path('upload/', views.upload, name='upload'),
    path('upload/add', views.add, name='add')
] 