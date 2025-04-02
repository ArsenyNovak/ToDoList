from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, FormView
from django.utils.timezone import now
from django.views.generic.edit import FormMixin

from .forms import AddTaskForm
from .models import Task


class HomePage(FormMixin,ListView):
    template_name = 'ToDoApp/index.html'
    form_class = AddTaskForm
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('home')
    extra_context = {
            'form': AddTaskForm,
            'text_article': 'На сегодня больше нет задач, ты молодец',
            'title_article': 'Задачи на сегодня',
    }

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_task = Task(description=form.cleaned_data['description'],
                        importance=form.cleaned_data['importance'],
                        time_running=form.cleaned_data['time_running']
                        )
        new_task.save()

        return HttpResponseRedirect(self.get_success_url())


    def get_queryset(self):
        return Task.objects.filter(time_running=now(), StatusTask=0)


class FuturePage(ListView):
    template_name = 'ToDoApp/list_task.html'
    model = Task
    context_object_name = 'tasks'
    extra_context = {
        'text_article': 'Будущее у тебя пока без заботное',
        'title_article': 'Задачи на будущее',
    }

    def get_queryset(self):
        return Task.objects.filter(time_running__gt=now())


class ArchvePage(ListView):
    template_name = 'ToDoApp/list_task.html'
    model = Task
    context_object_name = 'tasks'
    extra_context = {
        'text_article': 'ты пока ничего не сделал',
        'title_article': 'Выполненые задачи',
    }

    def get_queryset(self):
        return Task.objects.filter(time_running__lt=now())


class DeleteTask(DeleteView):
    template_name = 'ToDoApp/index.html'
    model = Task
    pk_url_kwarg = 'task_pk'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        del_task = Task.objects.get(pk=kwargs['task_pk'])
        del_task.delete()
        return HttpResponseRedirect(reverse_lazy('home'))

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


class RunningTask(View):

    def get(self, request, *args, **kwargs):
        update_task = Task.objects.get(pk=kwargs['task_pk'])
        update_task.StatusTask = 1
        update_task.save()
        return HttpResponseRedirect(reverse_lazy('home'))