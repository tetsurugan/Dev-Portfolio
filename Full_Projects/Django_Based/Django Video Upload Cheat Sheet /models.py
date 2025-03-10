from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    uploader = models.CharField(max_length=100)
    video_id = models.CharField(max_length=100, unique=True)  # Store YouTube video ID
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title