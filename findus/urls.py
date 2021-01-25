from django.contrib import admin
from django.urls import path
from findus import views

urlpatterns = [
    path('findus/', views.location, name="location"),
]
