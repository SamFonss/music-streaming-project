#!/usr/bin/env python

'''
This script defines data models
Includes models for audio files and user permissions.
'''

# Django imports
from django.db import models
import os

# Audio file model
class AudioFile(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to='audio/') # Folder within MEDIA_ROOT
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def delete(self, using=None, keep_parents=False):
        # Delete the file from the filesystem
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)  # Delete the file from storage
        super().delete(using=using, keep_parents=keep_parents)  # Call the parent's delete method

# Class for giving permissions to users
class Meta: 
    permissions = [
        ("can_upload", "Can upload files"),
    ]
