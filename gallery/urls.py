from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/like/', views.like_photo, name='like_photo'),
    path('photo/<int:pk>/dislike/', views.dislike_photo, name='dislike_photo'),
]