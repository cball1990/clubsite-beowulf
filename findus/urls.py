from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('findus/', views.location, name="location"),
]
