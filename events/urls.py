from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('events/', views.viewEvents, name="viewEvents"),
]
