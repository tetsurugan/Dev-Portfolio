from django.urls import path
from .views import video_list, add_video

urlpatterns = [
    path('', video_list, name='video_list'),
    path('add/', add_video, name='add_video'),
]