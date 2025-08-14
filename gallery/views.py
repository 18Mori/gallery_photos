from django.shortcuts import render, get_object_or_404
from .models import Photo, Tag
from django.template import loader  



def home(request):
  photo = Photo.objects.all()
  tags = Tag.objects.all()
  
  return render(request, 'home.html', {'photo': photo, 'tags': tags})

def photo_list(request, pk):
  photo = get_object_or_404(Photo, pk=pk)
  
  return render(request, 'photo_list.html', {'photo': photo})

