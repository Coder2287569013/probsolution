from django import forms
from home.models import Project, Task, TaskItem

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image']
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'project_id']
class TaskItemForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = ['text', 'project_id', 'task_id']
    def __init__(self,*args, **kwargs):
        super(TaskItemForm, self).__init__(*args, **kwargs)      
        project_id = self.instance.project_id
        self.fields['task_id'].queryset = Task.objects.filter(project_id=project_id)