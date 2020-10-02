from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy # url로 리다이렉션, get_absolute_url(), reverse() 등등 배워두면 유용하다고함.
from django.views.generic.list import ListView # 데이터 리스트 보기
from django.views.generic.detail import DetailView # 데이터 상세 보기
from django.views.generic.edit import CreateView, UpdateView, DeleteView # 데이터 추가, 수정, 삭제
from .models import ClassBlog

# 목록보기
# 어떤 모델의 데이터를 보여줄지만 정해주면된다.
# 나머지는 ListView가 알아서 처리해준다.
# 필요 html : 블로그 리스트를 담은 html : (소문자모델)_list.html 이 default로 자동으로 연결된다.
# template에서는 object_list라는 변수이름으로 알아서 모든 객체들을 담겨 있다.
class BlogView(ListView): 
    template_name = 'classcrud/list.html' # (소문자모델)_list.html (default) html 이름이 아닌 사용자가 html이름을 지정하여 연결할수있다.
    context_object_name = 'blog_list' # 템플릿에서 object_list라는 디폴트 변수명이 아닌 사용자가 지정한 객체명으로 사용가능하다.
    model = ClassBlog

# 자세히보기(상세보기)
# 필요 html : 상세 페이지를 담은 html : (소문자모델)_detail.html 이 default로 자동으로 연결된다.
# template에서는 object라는 변수이름으로 알아서 모든 객체들을 담겨 있다.
class BlogDetail(DetailView): 
    # context_object_name = 'blog' # 템플릿에서 object라는 디폴트 변수명이 아닌 사용자가 지정한 객체명으로 사용가능하다.
    model = ClassBlog

# 생성하기
# 어떤 모델인지, 입력받은 필드는 무엇인지, 성공시 어디로 리다이렉션하지 정해주면된다.
class BlogCreate(CreateView): # 필요 html : form(입력공간)을 갖고있는 html : (소문자모델)_form.html 이 default로 자동으로 연결된다.
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

# 수정하기
# 어떤 모델인지, 입력받은 필드는 무엇인지, 성공시 어디로 리다이렉션하지 정해주면된다.
class BlogUpdate(UpdateView): # 필요 html : form(입력공간)을 갖고있는 html : (소문자모델)_form.html 이 default로 자동으로 연결된다.
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

# 삭제하기
# 어떤 모델인지, 성공시 어디로 리다이렉션하지 정해주면된다.
class BlogDelete(DeleteView): # 필요 html : "이거 진짜 지울꺼야?" html : (소문자모델)_confirm_delete.html 이 default로 자동으로 연결된다.
    model = ClassBlog
    success_url = reverse_lazy('list')