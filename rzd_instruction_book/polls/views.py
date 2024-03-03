from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .utils import *
from . models import Question, Answer, Test
from . forms import *


class ChoiceTopic(ListView):
    model = Test
    template_name = 'polls/test.html'
    context_object_name = 'test_choice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_choice'] = get_object_or_404(Test, id=self.kwargs['topic_id'])
        context['question_list'] = get_object_or_404(Test, id=self.kwargs['topic_id']).questions.all()
        return context

# def choice_topic(request, topic_id):
#     test_choice = get_object_or_404(Test, pk=topic_id)
#     print(test_choice)
#     question_list = test_choice.questions.all()
#     print(question_list)
#     data = {
#         'question_list': question_list,
#         'test_choice': test_choice,
#
#     }
#
#     return render(request, 'polls/test.html', context=data)


class ShowTopicTests(ListView, DataMixin):
    model = Test
    context_object_name = 'topics_test'
    template_name = 'base.html'
    # extra_context = {'menu': menu}

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context() ## вызываем метод у миксина и присваиваем переменной
        context.update(c_def) ## обновляем context из mixin
        # context['menu'] = menu
        return context


#
def vote(request, question_id):
    # all_answer = question.answer_set.all()
    # print(all_answer)
    question = get_object_or_404(Question, pk=question_id)
    print(question)

    # print(selected_choice)
    right_answer = question.answer_set.get(right=True)
    # print(right_answer)
    try:
        selected_choice = question.answer_set.get(pk=request.POST['choice'])
        print(request.POST['choice'])
    except (KeyError, Answer.DoesNotExist):
        return HttpResponse('Выбирете ответ')
    else:
        if selected_choice.right is True:
            return render(request, 'polls/result_tests.html', {'selected_choice': selected_choice, 'question': question})
        else:
            return render(request, 'polls/result_tests.html', {'right_answer': right_answer, 'question': question})


# class Vote(ListView):
#     model = Question
#     template_name = 'polls/result_tests.html'
#
#     context_object_name = 'question'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['question'] = get_object_or_404(Question, pk = self.kwargs['question_id'])
#         context['selected_choice'] = get_object_or_404(
#             Question, pk = self.kwargs['question_id']).answer_set.get(pk=request.POST['choice'])
#         print(context)
#         return context

