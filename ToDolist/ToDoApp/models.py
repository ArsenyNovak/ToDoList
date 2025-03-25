from django.db import models

# Create your models here.
class Task(models.Model):

    class Status(models.IntegerChoices):
        IMPORTANT = 0, 'Срочное'
        OPTIONAL = 1, 'Не обязательное'


    description = models.TextField(verbose_name= 'Описание')
    importance = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.OPTIONAL)
    time_create = models.DateTimeField(auto_now_add=True)
    time_finish = models.DateTimeField(auto_now=True)
