from django.db import models
from django.contrib.auth.models import User



class Question(models.Model):
    text = models.CharField(max_length=500, verbose_name='Текст')
    num_right = models.IntegerField(verbose_name='Количество правильных ответов')

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=500, verbose_name='Ответ')
    right = models.BooleanField(default=False, verbose_name='Правильный')

    def __str__(self):
        return self.text


class Test(models.Model):
    title = models.CharField(max_length=300, verbose_name='Тема')
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    theory = models.CharField(max_length=1000, verbose_name='Теория')
    tests_s = models.ManyToManyField(Test)

    def __str__(self):
        return self.title

class Test_Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result = models.CharField(verbose_name='Результат', max_length=300)

    def __str__(self):
        return self.result