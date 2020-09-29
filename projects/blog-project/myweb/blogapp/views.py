from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

def blog_list(req):
    blogs = Blog.objects
    return render(req, 'blog_list.html', {"blogs" : blogs})

def blog_detail(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'blog_detail.html', {"blog" : blog})

def blog_write(req):
    return render(req, 'blog_write.html')

def create_blog(req):
    blog = Blog()
    blog.title = req.GET['title']
    blog.body = req.GET['body']
    blog.save()
    return redirect('/blog/detail/'+str(blog.id))

def blog_modify(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'blog_modify.html', {"blog" : blog})

def update_blog(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.title = req.GET['title']
    blog.body = req.GET['body']
    blog.save()
    return redirect('/blog/detail/'+str(blog.id))

def delete_blog(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('/blog/list/')