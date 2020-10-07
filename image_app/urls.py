from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('upload', views.upload),
    path('resize/<int:pk>', views.resize),
    url('index', views.index),
]