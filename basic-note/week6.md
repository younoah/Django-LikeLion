## form

- 기존의 HTML로 form을 일일히 만드는것이 아닌 Model형식에 맞는 입력공간을 장고에서 제공한다.

- form파일을 작성하는것은 model파일을 작성하는것과 비슷하다
- models.py가 DB에 연결되는것이라면
- form.py는 html의 form 태그와 연결되는것이다.

- form.py 두가지 입력공간을 만들수 있다.
  1. 모델을 기반한으로 한 입력공간 만들기 : `from django import forms.ModelForm`
  2. 임의의 입력공간 만들기 : `from django import forms.Form`



### 1. forms.py 작성하기

- 해당하는 앱폴더 안에 forms.py 파일을 생성한다.

#### 모델 기반 입력공간 만들기

```python
from django import forms.ModelForm

class MyForm(forms.ModelForm):
  class Meta:
    # 메타 클래스 안에서
    # 어떤 모델을 기반으로 한 입력 공간인지
    # 그 모델 중에서 어떤 항목을 입력받을것 인지를 명시한다.
#################################################
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
```

> 메타클래스란?
>
> 파이썬에서는 클래스도 결국 객체이다.
>
> 쉽게 말해 메타클래스는 클래스를 만드는 클래스이다.

#### (참고)임의의 입력공간 만들기

- 모델을 작성하듯이 내가 넣고싶은 필드를 작성하면 된다.

```python
from django import forms.ModelForm

class MyForm(forms.ModelForm):
  img = forms.ImageField()
  text = forms.TextField()
  time = forms.DateTimeField()
```



### 2. views.py 작성하기

- 뷰를 실행실키 url도 작성해야한다.

  ```python
  # urls.py
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('new', views.blogpost, name = 'new'),
  ]
  ```

```python
# views.py
from .form import MyForm

def create(req):
  # 수행 역할
  # 1. 처음 new.html에 들어갔을 때 빈 입력공간 띄우기 -> GET
  # 2. 이용자가 무엇인가 입력하면 그 입력값들 처리하기 -> POST
  # 1번과 2번과 구분하는 방법은 http 메서드 방식으로 구분한다. (GET이냐 POST이냐)
  # if req가 POST방식이면:
  #		2. 이용자가 입력한 입력값들 처리하기
  # else: (req가 GET방식이면)
  #		1. 빈 입력공간 띄우기
  
####################################
from .form import BlogForm
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
        return render(req, 'new.html', {'form' : form})
```

#### + 모델에 입력할 값중에 넣고 따로 입력공간을 만들고싶지 않을때

예를들어 블로그 프로젝트에서 블로그의 변수는 타이틀, 데이트, 바디가 있었는데 

타이틀과 바디만 입력받고 데이트는 자동으로 입력되게 하고싶다. 

이럴땐 타이틀과 바디만 입력받고 데이트는 따로 메서드를 구현해서 처리한다.

```python
from .form import MyForm

def create(req):
  # if req가 POST방식이면 : 
    # .is_valid(적절한 값이 잘 입력되었는지 확인)
    
    # 일단 저장하지 않은상태에서 form객체 말고 model객체에 접근하고 반환
    form.save(commit=False)
    
    model객체 안의 date변수에 접근하고 date변수에 값을 할당 
    model객체 저장
```

> .is_vaild()는 입력값이 잘 입력되었는지를 검사하는 메서드이다.
>
> 모든 입력값이 다 입력되었는지
>
> 모든 항목이 다 입력되었다면, 형식에 맞게 입력되었는지를 검사하는 메서드이다.
>
> 만일 모든 항목이 잘 입력되었다면 True를 반환하고
>
> 입력값에 문제가 있다면 Fasle를 반환한다.
>
> ---
>
> form.save(**commit=False**) 메서드는 일단 저장하지 않고 모델 객체를 반환하라는 의미이다.

### 3. HTML 작성

- form안의 내용을 어떤 태그로 감싼 채 출력할지 미리 결정이 가능하다.

```html
{{form}}을 이용하여 부르지만 그냥 부르면 이쁘게 출력이 안된다.
아래와같이 출력하면 태그에 맞춰서 보기 좋게 출력할수 있다.

{{form.as_table}} : form의 내용(입력공간)이 table(표)형식으로 풀력
{{form.as_p}} : form의 내용(입력공간)이 p(문단) 형식으로 출력
{{form.as_ul}} : form의 내용(입력공간)이 ul(리스트)형식으로 출력
```

```html
<div class="container">
    <form method="POST">
        {% csrf_token %}
        <table>
            {{form.as_table}}
        </table>
        <br>
        <input class="btn btn-dark" type="submit" value="작성완료">
    </form>
</div>
```

> form태그에 action="{% url 'url이름' %}" 왜 작성을 안하지??

