from django.shortcuts import render
from .models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'portfolio/project_index.html', context)

def project_detail(request, pk):
    # pk はプライマリーキーの事 IDと同じ意味
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_detail.html', context)