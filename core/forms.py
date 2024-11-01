#!/usr/bin/env python

'''
This script contains form definitions for user interactions.
Includes forms for uploading audio files.
'''

# Django imports
from django import forms

# App imports
from core.models import AudioFile

# Form for uploading audio files
class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['title', 'artist', 'file']
