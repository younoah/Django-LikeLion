## model & admin 

목표

- 모델에 데이터를 어떻게 담을 것인가
- 모델의 데이터를 어떻게 뷰로 넘길 것인가
- 그것을 어떻게 화면에 띄울 것인가

### model

models.py에서 class로 데이터 모델을 정의한다.

모델을 정의하고 나면 아래와 같이 명령어로 데이터베이스에게 데이터 모델을 등록해야한다.

```python
python manage.py makemigrations
pyrhon manage.py migrate
```

### 어드민 계정생성

```python
python manage.py createsuperuser
```

- admin.py에 데이터 등록하기

```python
# admin.py
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)
```

## 쿼리셋

- 모델로 부터 전달 받은 객체를 쿼리셋이라고한다.
- 모델.쿼리셋(objects) 를 쿼리셋이라고 한다.
- 모델.objects.메서드 를 이용하여 데이터를 처리할수 있다.