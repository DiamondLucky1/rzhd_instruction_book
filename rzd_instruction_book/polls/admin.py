from django.contrib import admin
from .models import Question, Answer, Test, Topic,Test_Result


class Answerinline(admin.TabularInline):
    model = Answer
    extra = 3


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'right', 'id')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'num_right', 'id')
    inlines = [Answerinline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Test)
admin.site.register(Topic)
admin.site.register(Test_Result)
