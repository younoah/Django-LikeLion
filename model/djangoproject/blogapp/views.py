from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(req):
    blogs = Blog.objects
    return render(req, 'index.html', {'blogs':blogs})