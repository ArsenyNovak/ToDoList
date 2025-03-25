from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

class HomePage(ListView):
    model = Task
    template_name = 'ToDoApp/index.html'
    extra_context = {'title': 'main'}

