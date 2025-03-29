from django.db import models
from django.urls import reverse
from django.utils.timezone import now
import datetime
# Create your models here.
class Task(models.Model):

    class StatusImportance(models.IntegerChoices):
        IMPORTANT = 0, 'Срочное'
        OPTIONAL = 1, 'Не обязательное'

    class Status(models.IntegerChoices):
        RUNNING= 0, 'Выполняется'
        COMPLETED = 1, 'Завершено'


    description = models.TextField(verbose_name= 'Описание')
    importance = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), StatusImportance.choices)),
                                       default=StatusImportance.OPTIONAL)
    StatusTask = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                     default=Status.RUNNING)
    time_create = models.DateTimeField(auto_now_add=True)
    time_running = models.DateField(default=now())
    time_finish = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('update_task', kwargs={'task_pk': self.pk})
