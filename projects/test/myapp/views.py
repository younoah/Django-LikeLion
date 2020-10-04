from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Blog

def home(req):
    return render(req, 'home.html')

class BlogList(ListView):
    model = Blog

class BlogDetail(DetailView):
    model = Blog

class BlogCreate(CreateView):
    model = Blog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('list')