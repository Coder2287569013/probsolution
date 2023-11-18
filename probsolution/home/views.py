from typing import Any
from django.shortcuts import render, redirect
from home.models import Project, Task, TaskItem
from django.views.generic import CreateView, DetailView
from home.forms import ProjectForm, TaskForm, TaskItemForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    task_items = TaskItem.objects.all()
    context = {
        'projects': projects,
        'tasks': tasks,
        'task_items': task_items
    }
    return render(request, 'home/index.html', context=context)

class CreateProjectView(CreateView):
    template_name = 'home/mk_project.html'
    form_class = ProjectForm

    def form_valid(self,form):
        data = form.data
        project = Project(name = data.get('name'))
        project.author = self.request.user
        project.save()
        return redirect('home-page')

class CreateTaskView(CreateView):
    template_name = 'home/mk_task.html'
    form_class = TaskForm

    def form_valid(self,form):
        data = form.data
        task = Task(text = data.get('text'), project_id_id = data.get('project_id'))
        task.save()
        return redirect('home-page')

class CreateTaskItemView(CreateView):
    template_name = 'home/mk_taskitem.html'
    form_class = TaskItemForm

    def form_valid(self,form):
        if form.is_valid():
            data = form.data
            taskitem = TaskItem(text = data.get('text'), project_id_id = data.get('project_id'), task_id_id = data.get('task_id'))
            taskitem.save()
        return redirect('home-page')

class ProjectPage(DetailView):
    model = Project
    template_name = 'home/project-page.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        context["tasks"] = Task.objects.filter(project_id=kwargs["object"])
        context["task_items"] = TaskItem.objects.all()
        return context
    