from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import FuncBlog
from .forms import BlogForm

#http메서드 get post put delete
#데이터다루기 create read update delete

# 불러오기
def read(req):
    blogs = FuncBlog.objects.all()
    return render(req, 'blog.html', {'blogs' : blogs})

# 생성하기
def create(req):
    if req.method == 'POST':
        form = BlogForm(req.POST)
        if form.is_valid():
            # 만약 모든프로퍼티 항목이 작성된거면 form.save()해도된다.
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('read') #혹은 주소 /func-blog
    else: # GET방식일때
        form = BlogForm()
        return render(req, 'form.html', {'form' : form})

# 수정하기
def update(req, pk):
    blog = get_object_or_404(FuncBlog, pk = pk)
    # 해당하는 블로그 객체 pk에 맞는 입력공간
    form = BlogForm(req.POST, instance=blog) #instance는 곧 객체 pk번쨰를 저장할수 있는 입력공간이다 라는 의미.
    if form.is_valid():
            form.save()
            return redirect('read')
    # 제대로 입력이 안됬거나 POST방식이 아니라면 아래를 실행
    return render(req, 'form.html', {'form':form})

# 삭제하기
def delete(req, pk):
    blog = get_object_or_404(FuncBlog, pk = pk)
    blog.delete()
    return redirect('read')