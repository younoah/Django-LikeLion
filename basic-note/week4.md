## 목차

- 블로그 프로젝트
  - pk
  - path converter
  - get_object_404

- 블로그 프로젝트 목표
  - 글을 클릭했을 때 detail.html 페이지 내보내기

## 블로그 글(객체)을 클릭했을 때 해당 객체의 detail.html 띄우기

![detail_design1](../images/detail_design.png)



### What to do

> pk(primary key) : 데이터 구분자, 객체들의 이름표, 대표값
>
> path Converter : URL을 계층적으로 디자인
>
> get_object_or_404 : pk로 객체를 구분지어서 갖고온다. 이때 객체가 없다면 404에러를 띄운다.



- **PK** : **x번째 블로그 객체**를 요청하면 x번 객체 내용 띄우기

  ![pathConverter](../images/pathConverter.png)

  

- **path Converter** : URL 설계 - **우리사이트/blog/객체번호(x)**

  ```python
  # (home.html)
  <a href="{% url 'detail' blog.id %}"><h2>{{blog.title}}</h2></a>
  ## {% url %}의 마지막 인자값은 해당 객체의 id값은 urls.py로 넘긴다.
  
  # (urls.py)
  path('blog/<int:blog_id>, blog.views.detail, name = "detail"')
  ## {% url %}에서 넘겨 받은 객체의 id값으로 path Converter를 생성한다.
  ```

  - "사이트이름/blog/**정수**"형태로 url을 설계하겠다.

  - blog_id는 blog.views.detail이라는 메서드에게 넘기는 인자이다. 

    >  detail이라는 메서드는 몇번객체 라는 정보가 필요하기 떄문

  

- **get_object_or_404** : pk로 객체를 구분지어서 갖고온다. 이때 객체가 없다면 **404에러**를 띄운다.

  ```python
  from django.shortcuts import render, get_object_or_404
  
  def detial(req, blog_id):
    blog_detial = get_object_or_404(Blog, pk = blog_id)
    # get_object_or_404(모델클래스명, pk = pathConverter)
  ```

  

## 글 작성하기 구현 (Create)

 ![createLogic](../images/createLogic.png)



- new.html

```html
<div class="container">
    <form action="{% url 'create' %}">
        <h4>제목</h4>
        <input type="text" name="title">
      	// title이라는 이름으로 데이터에 접근
        <br>
        <br>
        <h4>본문</h4>
        <textarea name="body" cols="40" rows="10"></textarea> 
      	// body라는 이름으로 데이터에 접근
        <br>
        <br>
        <input class="btn btn-dark" type="submit" value="제출하기">
    </form>
</div>
```

- views.py

```python
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def new(req):
    return render(req, 'new.html')

def create(req):
    blog = Blog() #Blog 객체 생성
    blog.title = req.GET['title'] #객체의 타이틀에 폼에서 title이라는 이름으로 데이터를 갖고와저장
    # blog.created_at = timezone,datetime.now() # 모델생성시 자동저장으로 했기때문에 굳이 안해도됨
    blog.body = req.GET['body'] #객체의 타이틀에 폼에서 title이라는 이름으로 데이터를 갖고와저장
    blog.save() # 지금까지 입력한 객체를 저장
    return redirect('/blog/'+str(blog.id)) 
```

> #### redirect vs render
>
> - redirect는 특정 페이지를 호출한다. 외부에 있는 웹까지 호출할수 있다.
>
> - render는 우리 프로젝트의 html만 호출할수 있지만 html로 데이터를 넘겨줄수 있다.



- urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name = 'home'),
    path('blog/<int:blog_id>', blogapp.views.detail, name = 'detail'),
    path('blog/new', blogapp.views.new, name = 'new'), # new 메서드 실행 -> new.html만 연다
    path('blog/create', blogapp.views.create, name = 'create'), 
  	# create 메서드 실행 (단순히 메서드만 실행시키기 위한 URL이다.)
]
```

