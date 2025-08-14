from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
      return self.name
class Photo(models.Model):
  tital = models.CharField(max_length=50)
  description = models.TextField(blank=True)
  image = CloudinaryField('image', blank=True)
  tags = models.ManyToManyField(Tag, blank=True)
  likes = models.ManyToManyField(User, related_name='photo_likes', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
      return self.tital
    
class userProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True)
  
  def __str__(self):
    return self.user.username
  