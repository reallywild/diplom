from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    full_name = models.CharField(max_length=254, verbose_name="ФИО", blank=False)
    username = models.CharField(max_length=254, verbose_name="Логин", blank=False, unique=True)
    email = models.EmailField(max_length=254, verbose_name="Почта", blank=False, unique=True)
    password = models.CharField(max_length=254, verbose_name="Пароль", blank=False)

class News(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название", blank=False, null=False)
    description = models.CharField(max_length=254, verbose_name="Описание", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    set_time = models.DateTimeField(default=timezone.now(), verbose_name='Выбрать время', blank=False, null=False)
    image = models.ImageField(upload_to='post_images/', default='none')

    class Meta:
        ordering=["-set_time"]

class Service(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название", blank=False, null=False)
    description = models.CharField(max_length=254, verbose_name="Описание", blank=False, null=False)

class Vacancy(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название", blank=False, null=False)
    description = models.CharField(max_length=254, verbose_name="Описание", blank=False, null=False)
    salary = models.CharField(max_length=254, verbose_name="Зарплата", blank=False, null=False)
    location = models.CharField(max_length=254, verbose_name="Местоположение", blank=False, null=False)