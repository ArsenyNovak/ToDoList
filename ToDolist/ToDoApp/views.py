from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView

from .forms import AddTaskForm
from .models import Task


class HomePage(ListView):
    template_name = 'ToDoApp/index.html'
    model = Task
    context_object_name = 'tasks'
    extra_context = {
            'title': 'Задания на сегодня'
    }

    # def get_queryset(self):
    #     return Task.objects.filter(is_published=True)

class CreateTask(CreateView):
    template_name = 'ToDoApp/addTask.html'
    form_class = AddTaskForm
    extra_context = {
        'title': 'Добавление задачи',
        'ButtonSubbmit': 'Добавить задачу'
    }
    success_url = reverse_lazy('home')

class UpdateTask(UpdateView):
    template_name = 'ToDoApp/updateTask.html'
    form_class = AddTaskForm
    model = Task
    pk_url_kwarg = 'task_pk'
    extra_context = {
        'title': 'Редактирование задачи',
        'ButtonSubbmit': 'Сохранить'
    }
    success_url = reverse_lazy('home')

class DeleteTask(DeleteView):
    template_name = 'ToDoApp/index.html'
    model = Task
    pk_url_kwarg = 'task_pk'
    success_url = reverse_lazy('home')
