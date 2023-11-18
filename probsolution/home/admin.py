from django.contrib import admin
from home.models import Project, Task, TaskItem

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskItem)