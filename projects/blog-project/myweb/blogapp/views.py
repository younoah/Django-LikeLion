from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .form import BlogForm

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

##form을 이용한 생성
def blogpost(req):
    if req.method == 'POST':
        form = BlogForm(req.POST) # req.POST내용을 form에 담아준다.
        if form.is_valid():
            blog = form.save(commit = True) # 저장(커밋)하진않고 모델 객체를 불런온다.
            blog.created_date = timezone.now()
            blog.save()
            return redirect('/blog/detail/'+str(blog.id))
    else:
        form = BlogForm()
        return render(req, 'blog_write.html', {'form' : form})