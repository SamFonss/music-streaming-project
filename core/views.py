#!/usr/bin/env python #

'''
This script contains views for handling user requests
Includes functionality for uploading, browsing, and streaming audio files
'''
import os

# Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse



# App imports
from core.forms import AudioFileForm
from core.models import AudioFile


# Login view
def login_view(request):
    return auth_views.LoginView.as_view(template_name='registration/login.html')(request)

# Upload view
def upload_file(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            Audio_file=form.save()
            messages.success(request, 'File uploaded successfully!')
            # Debug information
            print(f"Uploaded file path: {Audio_file.file.path}")  
            return redirect('upload')  
    else:
        form = AudioFileForm()
    return render(request, 'upload.html', {'form': form})

# Menu view
def menu(request):
    # Redirects logged in users to their page even if guest is selected   
    if request.user.is_authenticated and request.GET.get('guest') == 'true':
        return redirect('menu')
    
    is_guest = request.GET.get('guest') == 'true'
    can_upload = not is_guest and request.user.has_perm('core.can_upload')
    return render(request, 'menu.html', {'can_upload': can_upload,
                                         'is_guest': is_guest})


# Browse View
def browse(request):

    is_guest = request.GET.get('guest') == 'true'
    can_upload = not is_guest and request.user.has_perm('core.can_upload')
    
    # Retrieves all audio files
    audio_files = AudioFile.objects.all()  
    audio_files_with_formats = []
    
    for audio in audio_files:
        print(f"Download URL for {audio.title}: {audio.file.url}")
        # Generates URLs for each format
        audio_data = {
            'id': audio.id,
            'title': audio.title,
            'artist' : audio.artist,
            'uploaded_at': audio.uploaded_at,
            'mp3_url': audio.file.url,
            'wav_url': audio.file.url.replace('.mp3', '.wav'),
            'm4a_url': audio.file.url.replace('.mp3', '.m4a'),  
        }
        audio_files_with_formats.append(audio_data)
        
    return render(request, 'browse.html', {'audio_files': audio_files_with_formats,
                                           'can_upload': can_upload,'is_guest': is_guest})

@login_required
def delete_file(request, file_id):
    audio_file = get_object_or_404(AudioFile, id=file_id)
    
    # Checks if user has permission to delete
    if request.user.has_perm('core.can_upload'):
        # Deletes the file from the storage and database
        audio_file.delete()  
        messages.success(request, 'File deleted successfully!')

    return HttpResponseRedirect(reverse('browse'))  # Redirects to browse page
        
   

  
