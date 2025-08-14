from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('photo/<int:pk>/', views.photo_list),
    path('like/<int:pk>/', views.like_photo),
    path('dislike/<int:pk>/', views.dislike_photo),
]