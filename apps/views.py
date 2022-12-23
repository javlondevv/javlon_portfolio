from django.core.paginator import Page
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from apps.models import Portfolio, User, WhatIDo
from apps.forms import  ContactForm

class MainPage(CreateView):
    model = Portfolio
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user'] = User.objects.filter(username='javlon').first()
        context['portfolio'] = Portfolio.objects.all()
        context['whatido'] = WhatIDo.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)



