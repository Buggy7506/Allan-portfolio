from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Project
from .forms import ContactForm


# -----------------------------
# Health / Ping endpoint
# -----------------------------
def ping(request):
    return HttpResponse("pong", content_type="text/plain")


# -----------------------------
# Home / Portfolio page
# -----------------------------
def index(request):
    # Order projects (newest first is common)
    projects = Project.objects.all().order_by('-id')
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Future: email / DB persistence
            print("Form submitted:", form.cleaned_data)
            form = ContactForm()  # reset after submit

    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'form': form,
    })


# -----------------------------
# Like project (POST only)
# -----------------------------
@require_POST
def like_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.likes = project.likes + 1
    project.save(update_fields=['likes'])
    return redirect('index')
