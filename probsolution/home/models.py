from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=256,null=False,blank=False)
    image = models.ImageField(null=True, blank=True, default='D:\\Projects\\probsolution\\probsolution\\media\\NoneImage.jpg', upload_to='projects/')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
class Task(models.Model):
    text = models.TextField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.text}"
class TaskItem(models.Model):
    text = models.TextField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE,default=1)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.text}"