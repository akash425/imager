from django.urls import path
from .views import input



urlpatterns=[
    path('', input.as_view(), name='input'),
]