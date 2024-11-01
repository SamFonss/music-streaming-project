#!/usr/bin/env python #

'''
This script contains views for handling user requests
Includes functionality for uploading, browsing, and streaming audio files
'''

# Django imports
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            print(f"Uploaded file path: {Audio_file.file.path}")  # Debug information
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
    return render(request, 'menu.html', {'can_upload': can_upload, 'is_guest': is_guest})
    # Determine upload permission based on guest status or user permissions
    can_upload = not is_guest and request.user.has_perm('core.can_upload')
    
    return render(request, 'menu.html', {'can_upload': can_upload, 'is_guest': is_guest})

# Browse View
def browse(request):
    # Retrieve all audio files
    audio_files = AudioFile.objects.all()  
    audio_files_with_formats = []
    
    for media in audio_files:
        # Generate URLs for each format
        audio_data = {
            'title': media.title,
            'artist' : media.artist,
            'uploaded_at': media.uploaded_at,
            'mp3_url': media.file.url,
            'wav_url': media.file.url.replace('.mp3', '.wav'),
            'm4a_url': media.file.url.replace('.mp3', '.m4a'),  
        }
        audio_files_with_formats.append(audio_data)
        
    return render(request, 'browse.html', {'audio_files': audio_files_with_formats})

