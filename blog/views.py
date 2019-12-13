from math import ceil

from django.shortcuts import render, redirect

# Create your views here.
from blog.forms import ProjectForm, HobbyForm
from blog.models import Project, ProjectCharacteristic, Hobby


def index(request):
    return render(request, 'index.html')


def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects_list})


def store_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)

        if project_form.is_valid():
            project_form.save()

        for key, characteristic in request.POST.items():
            if "characteristic-" in key:
                project_characteristic = ProjectCharacteristic(text=characteristic, project=project_form.instance)
                project_characteristic.save()
    return redirect('projects')


def remove_project(request):
    project_id = request.GET.get('project_id')

    project = Project.objects.get(id=project_id)
    project.delete()

    return redirect('projects')


def studies(request):
    return render(request, 'studies.html')


def hobbies(request):
    hobbies_list = Hobby.objects.all()

    return render(request, 'hobbies.html', {'hobbies': hobbies_list})


def store_hobby(request):
    if request.method == 'POST':
        hobby_form = HobbyForm(request.POST, request.FILES)

        if hobby_form.is_valid():
            hobby_form.save()

    return redirect('hobbies')