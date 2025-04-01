from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView

from .form import AddTaskForm
from .models import Task


def homepage(request):
    if  request.method == 'POST':
        time_running = [request.POST['time_running_year'],
                        request.POST['time_running_month'],
                        request.POST['time_running_day'],
                        ]
        time_running = '-'.join(time_running)
        new_task = Task(description= request.POST['description'],
                        importance=request.POST['importance'],
                        time_running=time_running
                        )
        new_task.save()

    extra_context = {
        'form': AddTaskForm,
        'tasks': Task.objects.all(),
        'title': 'Задания на сегодня'
    }
    return render(request, 'ToDoApp/index.html', extra_context)

def deletetask(request, task_pk):
    del_task = Task.objects.get(pk=task_pk)
    del_task.delete()
    return HttpResponseRedirect(reverse_lazy('home'))

# class CreateTask(CreateView):
#     template_name = 'ToDoApp/addTask.html'
#     form_class = AddTaskForm
#     extra_context = {
#         'title': 'Добавление задачи',
#         'ButtonSubbmit': 'Добавить задачу'
#     }
#     success_url = reverse_lazy('home')
#
# class UpdateTask(UpdateView):
#     template_name = 'ToDoApp/updateTask.html'
#     form_class = AddTaskForm
#     model = Task
#     pk_url_kwarg = 'task_pk'
#     extra_context = {
#         'title': 'Редактирование задачи',
#         'ButtonSubbmit': 'Сохранить'
#     }
#     success_url = reverse_lazy('home')
#
# class DeleteTask(DeleteView):
#     template_name = 'ToDoApp/index.html'
#     model = Task
#     pk_url_kwarg = 'task_pk'
#     success_url = reverse_lazy('home')
