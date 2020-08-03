from django.urls import path
from . import views


urlpatterns = [

    path('', views.homePage, name='homePage'),
    path('home/', views.home, name='home'),
    path('profile/', views.userProfile, name='profile'),

    path('register/', views.registerPage, name='register'),
    path('users/', views.allUser, name='users'),
    path('updateuser/<str:pk>/', views.updateUser, name='update_user'),
    path('deleteuser/<str:pk>/', views.deleteUser, name='delete_user'),

    path('address/', views.address, name='address'),

    path('update_address/<str:pk>/', views.address, name='update_address'),
    path('delete_address/<str:pk>/', views.address, name='delete_address'),

    path('profile/', views.profile, name='profile'),
    path('finance/', views.finance, name='finance'),


]
