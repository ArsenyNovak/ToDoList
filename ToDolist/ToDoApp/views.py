from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView

from .forms import AddTaskForm
from .models import Task


class HomePage(FormView):
    template_name = 'ToDoApp/index.html'
    form_class = AddTaskForm
    success_url = reverse_lazy('home')
    extra_context = {
            'tasks': Task.objects.all(),
    }

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        new_task = Task(description= form.cleaned_data["description"],
                       importance= form.cleaned_data["importance"],
                       time_running=form.cleaned_data["time_running"]
                    )
        new_task.save()
        self.get_context_data()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        kwargs = {**kwargs, **self.extra_context}
        """Insert the form into the context dict."""
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context_data(**kwargs)

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