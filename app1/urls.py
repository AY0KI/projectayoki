from django.urls import path
from django.urls.conf import include
from app1 import views

urlpatterns = [
   
  path('',views.index),
]
