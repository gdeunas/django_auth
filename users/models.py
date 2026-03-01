# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', null=True, blank=True,
                               help_text='загрузите свой аватар')
    phone_number = models.CharField(max_length=11, verbose_name='номер телефона', blank=True, null=True,
                                    help_text='введите номер телефона')
    country = models.CharField(max_length=40, verbose_name='страна', help_text='введите страну')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

