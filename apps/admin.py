from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html

from apps.models import User, Portfolio, Contact, WhatIDo


@admin.register(User)
class User(ModelAdmin):
    list_display = ('first_name', 'email', 'image', 'biography', 'delivered', 'year_experience')
    list_display_links = ('first_name',)


@admin.register(Portfolio)
class Portfolio(ModelAdmin):
    list_display = ('title', 'image', 'description', 'github_link')
    list_display_links = ('title',)
    exclude = ('slug',)


@admin.register(Contact)
class Contact(ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_display_links = ('name',)


@admin.register(WhatIDo)
class WhatIDo(ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title',)
