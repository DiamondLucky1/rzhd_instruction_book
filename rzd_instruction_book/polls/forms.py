from django import forms
from .models import *

class TestForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        q = Question.objects.get(id=1)
        self.fields['question'].emty_label = "Вопрос"

    class Meta:
        model = Answer
        fields = ['question', 'text', 'right']
