from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    """Display all uploaded videos"""
    videos = Video.objects.all().order_by('-added_on')
    return render(request, 'videos/video_list.html', {'videos': videos})

def add_video(request):
    """Allow users to add a new YouTube video"""
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'videos/add_video.html', {'form': form})