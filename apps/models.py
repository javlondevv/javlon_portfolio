from django.contrib.auth.models import AbstractUser

from django.db.models import EmailField, CharField, ImageField, TextField, IntegerField, Model, TextChoices, ForeignKey, \
    SET_NULL
from django.utils.text import slugify


class User(AbstractUser):
    email = EmailField(max_length=255, unique=True)
    phone = CharField(max_length=255, unique=True)
    image = ImageField(upload_to='%m', null=True, blank=True, max_length=300)
    biography = TextField(null=True, blank=True)
    age = CharField(max_length=5)
    degree = CharField(max_length=50)
    do = TextField(null=True, blank=True)
    year_experience = CharField(max_length=10)
    delivered = CharField(max_length=10, blank=True, null=True)

    # status = CharField(max_length=50, choices=Status.choices, default=Status.Junior)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Portfolio(Model):
    image = ImageField(upload_to='%m')
    title = CharField(max_length=80, blank=True, null=True)
    description = TextField(blank=True, null=True)
    github_link = CharField(max_length=255)


class Contact(Model):
    name = CharField(max_length=80, blank=True, null=True)
    email = EmailField(max_length=255, unique=True)
    message = TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class WhatIDo(Model):
    title = CharField(max_length=255, blank=True, null=True)
    description = TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'WhatIDo'
        verbose_name_plural = 'WhatIDO'
