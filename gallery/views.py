from django.shortcuts import render, redirect, get_object_or_404
from urllib3 import request
from .models import Photo, Tag, userProfile 
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import PhotoForm
from .models import Photo, Tag

def home(request):
  photos = Photo.objects.all()
  tags = Tag.objects.all()
  return render(request, 'home.html', {'photos': photos, 'tags': tags})

def increment_view_count(photo):
    photo.view_count += 1
    photo.save()

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.user.is_authenticated:
        if request.user == photo.uploader:
            increment_view_count(photo)
    else:
        return redirect('login')
    return render(request, 'photo_detail.html', {'photo': photo})

@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
      
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      remember_me = request.POST.get('remember_me',False)
      user = authenticate(request, username=username, password=password)

      if user is not None:
          auth_login(request, user)
          if remember_me:
              request.session.set_expiry(1209600)  # 2 weeks
          return redirect('home')
      else:
          messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

@login_required
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)
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
  user_photos = Photo.objects.filter(uploader=request.user).order_by('-created_at')
  context = {
      'form': form,
      'profile': profile,
      'user_photos': user_photos,
  }
  return render(request, 'registration/profile.html', context)

@require_POST
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def add_photo(request):
  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    if form.is_valid():
      photo = form.save(commit=False)
      photo.uploader = request.user
      photo.save()
      form.save_m2m()
      return redirect('photo_detail', pk=photo.pk)
  else:
    form = PhotoForm()
  return render(request, 'add_photo.html', {'form': form})
