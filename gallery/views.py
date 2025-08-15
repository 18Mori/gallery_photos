from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Tag, userProfile 
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login




def home(request):
  photo = Photo.objects.all()
  tags = Tag.objects.all()
  return render(request, 'home.html', {'photo': photo, 'tags': tags})

def photo_detail(request, pk):
  photo = get_object_or_404(Photo, pk=pk)
  return render(request, 'photo_detail.html', {'photo': photo})

@login_required
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
    photo.likes.add(request.user)
    return redirect('photo_detail', pk=pk)
  
@login_required
def dislike_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
    photo.dislikes.add(request.user)
    return redirect('photo_detail', pk=pk)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})
  
@login_required
def profile(request):
  try:
    profile = request.user.userprofile
  except userProfile.DoesNotExist:
    profile = userProfile.objects.create(user=request.user)
    
  if request.method == 'POST':
    form = UserProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile')
  else:
    form = UserProfileForm(instance=profile)
  return render(request, 'registration/profile.html', {'form': form})