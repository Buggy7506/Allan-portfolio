from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import F

from .models import Project
from .forms import ContactForm


# -----------------------------
# Health check
# -----------------------------
def ping(request):
    return HttpResponse("pong", content_type="text/plain")


# -----------------------------
# Home / Portfolio page
# -----------------------------
def index(request):
    # Fetch projects (newest first)
    projects = Project.objects.all().order_by('-id')

    # 🔥 Increment views atomically (safe for concurrency)
    Project.objects.update(views=F('views') + 1)

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Future: email / persistence
            print("Form submitted:", form.cleaned_data)
            form = ContactForm()

    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'form': form,
    })


# -----------------------------
# AJAX Like Project (POST only)
# -----------------------------
@require_POST
def like_project_ajax(request, pk):
    project = get_object_or_404(Project, pk=pk)

    # 🔥 Atomic increment
    Project.objects.filter(pk=pk).update(likes=F('likes') + 1)

    # Refresh value
    project.refresh_from_db(fields=['likes'])

    return JsonResponse({
        'likes': project.likes
    })
