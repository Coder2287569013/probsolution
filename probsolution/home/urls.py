from django.urls import path
from home.views import *

urlpatterns = [
    path('',homepage,name="home-page"),
    path('mk-project/', CreateProjectView.as_view(), name="mkproject"),
    path('mk-task', CreateTaskView.as_view(), name = "mktask"),
    path('mk-taskitem', CreateTaskItemView.as_view(), name = "mktaskitem"),
    path('project/<pk>', ProjectPage.as_view(), name="projectpage"),
]