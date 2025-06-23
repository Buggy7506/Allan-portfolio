from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project
from .forms import ContactForm

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
