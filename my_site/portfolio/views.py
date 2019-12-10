from django.shortcuts import render
from .models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }

    return render(request, 'projects/project_index.html', context)