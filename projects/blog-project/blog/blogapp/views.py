from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(req):
    blogs = Blog.objects
    return render(req, 'home.html', {"blogs" : blogs})

def detail(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'detail.html', {"blog" : blog})

def new(req):
    return render(req, 'new.html')

def create(req):
    blog = Blog()
    blog.title = req.GET['title']
    # blog.created_at = timezone,datetime.now()
    blog.body = req.GET['body']
    blog.save()
    return redirect('/blog/'+str(blog.id))
