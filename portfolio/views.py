from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ContactForm
from django.http import HttpResponse

# Ping Page
def ping(request):
    return HttpResponse("pong")

def index(request):
    projects = Project.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In future: send email / store message
            print("Form submitted:", form.cleaned_data)
            form = ContactForm()  # Reset form after submission

    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'form': form
    })

# ✅ New like view
def like_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.likes += 1
    project.save()
    return redirect('index')
