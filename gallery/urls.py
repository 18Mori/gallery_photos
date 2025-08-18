from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('photo/add/', views.add_photo, name='add_photo'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
]