from django.shortcuts import render
from .models import Project, Structure

# Create your views here.
def home(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {'projects':projects})

def structure(request):
    persons = Structure.objects.all()
    return render(request, "structure.html", {'persons':persons})

def project_detail_view(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, "detail_project.html", {'project':project})


def contact(request):
    return render(request, "contact.html")
