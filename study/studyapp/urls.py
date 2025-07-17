from django.urls import path
from . import views

urlpatterns= [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('createroom/', views.createroom, name='create-room'),
    path('updateroom/<str:pk>/', views.updateroom, name='update-room'),
    path('deleteroom/<str:pk>/', views.deleteroom, name='delete-room'),
    path('deletemessage/<str:pk>/', views.deleteMessage, name='delete-message')
    ]