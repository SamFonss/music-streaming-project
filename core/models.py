#!/usr/bin/env python

'''
This script defines data models
Includes models for audio files and user permissions.
'''

# Django imports
from django.db import models


# Audio file model
class AudioFile(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to='audio/') # Folder within MEDIA_ROOT
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Class for giving permissions to users
class Meta: 
    permissions = [
        ("can_upload", "Can upload files"),
    ]
