from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name = 'home'),
    path('profile/<str:pk>/', views.userProfile, name = 'profile'), 
    path('update-user/<str:pk>/', views.updateUser, name = 'updateUser'),
    path('room/<str:pk>/', views.room, name = 'room'),
    path('create-room/', views.createRoom, name = 'createRoom'),
    path('update-room/<str:pk>/', views.updateRoom, name = 'updateRoom'),
    path('delete-room/<str:pk>/', views.deleteRoom, name = 'deleteRoom'),
    path('delete-message/<str:pk>/', views.deleteMessage, name = 'deleteMessage'),
]