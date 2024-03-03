from polls.models import *
from instruction.models import *

menu = [{"title": "Инструкции", "url_name": "instruction"},
        {"title": "Электрические и пневмотческие схемы электропоезда", "url_name": "scheme"},
        {"title": "Неисправности электропоезда", "url_name": "malfunctions"},
]

class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                question = Question.objects.all()
                context['menu'] = menu
                context['question'] = question
                return context