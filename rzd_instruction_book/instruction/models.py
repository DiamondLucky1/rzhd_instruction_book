from django.db import models
from django.urls import reverse


class Instruction(models.Model):
    title = models.CharField(max_length=100, verbose_name='Инструкция')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instruction_show', kwargs={'inst_slug': self.slug})


class Sсheme(models.Model):
    name = models.CharField(max_length=100, verbose_name='Электрические схемы')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Изображения")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('scheme_show', kwargs={'scheme_slug': self.slug})


class Malfunctions(models.Model):
    name = models.CharField(max_length=100, verbose_name='Неисправности')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Содержание')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Изображения")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('malfunctions_show', kwargs={'malfunctions_slug': self.slug})
