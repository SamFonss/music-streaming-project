from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from core.forms import AudioFileForm
from django.contrib.auth.decorators import login_required
from core.models import AudioFile
from django.contrib import messages


def login_view(request):
    return auth_views.LoginView.as_view(template_name='registration/login.html')(request)

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

def menu(request):
       # Redirect authenticated users accessing "guest=true" to a regular menu view
    if request.user.is_authenticated and request.GET.get('guest') == 'true':
        return redirect('menu')

    is_guest = request.GET.get('guest') == 'true'
    can_upload = not is_guest and request.user.has_perm('core.can_upload')
    return render(request, 'menu.html', {'can_upload': can_upload, 'is_guest': is_guest})
    
    # Determine upload permission based on guest status or user permissions
    can_upload = not is_guest and request.user.has_perm('core.can_upload')
    
    return render(request, 'menu.html', {'can_upload': can_upload, 'is_guest': is_guest})

def browse(request):
    
    return render(request, 'browse.html')
