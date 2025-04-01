from django import forms

from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'importance', 'time_running']
        widgets = {
            'description': forms.Textarea(attrs={"cols": 50, "rows": 3, 'class': "item_form"}),
            'time_running': forms.SelectDateWidget(),
            # 'importance': forms.ChoiceWidget
        }