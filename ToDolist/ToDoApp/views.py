from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView

from .forms import AddTaskForm
from .models import Task


class HomePage(ListView):
    template_name = 'ToDoApp/index.html'
    model = Task
    context_object_name = 'tasks'
    #form_class = AddTaskForm
    #success_url = reverse_lazy('home')
    extra_context = {
            'form': AddTaskForm,
    }

    def post(self, request, *args, **kwargs):
        time_running = [request.POST['time_running_year'],
                        request.POST['time_running_month'],
                        request.POST['time_running_day'],
                        ]
        time_running = '-'.join(time_running)
        new_task = Task(description=request.POST['description'],
                        importance=request.POST['importance'],
                        time_running=time_running
                        )
        new_task.save()
        return HttpResponseRedirect(reverse_lazy('home'))



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

    # def get(self, request, *args, **kwargs):
    #     """Handle GET requests: instantiate a blank version of the form."""
    #     return self.render_to_response(self.get_context_data())
    #
    # def post(self, request, *args, **kwargs):
    #     """
    #     Handle POST requests: instantiate a form instance with the passed
    #     POST variables and then check if it's valid.
    #     """
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)