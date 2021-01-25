from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('confirmed/', views.confirmed, name="confirmed"),
    path('logout', views.logout, name="logout"),
    path('account/', views.account, name="account"),
    path('updateimage/<int:userImage_id>', views.updateimage, name="updateimage"),
    path('deleteevent/<int:events_id>', views.deleteEvent, name="deleteevent"),
    path('addevent/', views.add_event, name="addevent"),
]
