from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
      return self.name
class Photo(models.Model):
  title = models.CharField(max_length=50)
  uploader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  description = models.TextField(blank=True)
  image = CloudinaryField('image', blank=True, null=True)
  tags = models.ManyToManyField(Tag, blank=True)
  likes = models.ManyToManyField(User, related_name='photo_likes', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  view_count = models.PositiveIntegerField(default=0)
    
def __str__(self):
      return self.title

class userProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True)
  
  def __str__(self):
    return self.user.username
  
  @property
  def uploaded_photos_count(self):
    return Photo.objects.filter(uploader=self.user).count()
  
