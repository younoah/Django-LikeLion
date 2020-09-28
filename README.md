## 목차

- [나의 설정](#내가-설정한-파이썬/터미널(zsh)/vscode-세팅)
- [찾아보기](#찾아보기)
- [문제해결 완료](#문제해결-완료)
- [장고 치트시트](#치트시트)

## 내가 설정한 파이썬/터미널(zsh)/vscode 세팅

- zsh 설정

  > code ~/.zshrc 에서
  >
  > alias python=/usr/local/bin/python3
  >
  > alias pip=/usr/local/bin/pip3
  >
  > 추가함- python3 에서 python 이라고 처도 python3가 실행되도록 설정
  >
  > (이 밖에 zsh관련 설정은 ~/.zshrc 여기서 확인할수 있다.)
  >
  > ---
  >
  > 위 설정은 하니깐 가상환경에 들어가서 python 명령어를 치면 가상환경 경로의 python이 아닌 
  >
  > /usr/local/bin/python3이 실행되버린다.
  > alias가 되어있어서 저절로 경로를 잡아 버리는거 같다...
  >
  > 따라서 일단 위에 alias 설정은 꺼두었다.

- beautify : cmd + shift + L
  
  - prettier 가 더 섬세한것같아서 차근차근 알아보기



## 찾아보기

- 장고 프로젝트, 폴더, 파일 명명법

- 장고/파이썬 refactor, 변수/폴더명/파일명 변경시 알아서 세팅다시되도록 하는게 있을까?

- 남의 작업한 장고프로젝트를 갖고와서 해당 장고프로젝트에 맞는 가상환경 생성방법

- 맥, 파이썬 업데이트, 파이썬 인터프리터 선택

- python select interpreter 설정 개념 

  

## 문제해결 완료

파이썬 가상환경, 버전 개념(중요)

> https://dojang.io/mod/page/view.php?id=2470
>
> https://seolin.tistory.com/96
>
> https://wikidocs.net/16402

![python_venv](./images/python_venv.png?lastModify=1601309952)

맥 vscode, 파이썬 세팅, 장고세팅(models.modle 자동완성), 왜 가상환경에 장고가 미리 설치되어있다 뜨는지

![vscode_error](./images/vscode_error.png?lastModify=1601309952)

![vscode_eroor2](./images/vscode_eroor2.png?lastModify=1601309952)

![pylintererror](./images/pylintererror.png?lastModify=1601309952)

![pylinterror2](./images/pylinterror2.png?lastModify=1601309952)

![pylinterror3](./images/pylinterror3.png?lastModify=1601309952)

![pylinsterror4](./images/pylinsterror4.png?lastModify=1601309952)

![pylinterror5](./images/pylinterror5.png?lastModify=1601309952)

> 파이썬 인터프리터가 어떤것으로 잡혀있나에 따라 파이썬을 아예 인식을 못하는 경우도 있다.



## 치트시트

- 장고프로젝트를 담은 디렉터리 생성후 해당 디렉터리를 vscode로 실행
- 가상환경 설정

```python
python -m venv <가상환경이름>
```

- 가상환경 실행

```
// in mac
source <가상환경이름>/bin/activate
// in window
source <가상환경이름>/scripts/activate

// 가상환경 종료
deactivate
```

- 장고 설치

```
pip install djanog

// 특정 버전의 장고 설치
pip install django==2.1.3

// 장고 삭제
pip uninstall django
```

> pip 패키지란?
>
> - 파이썬으로 작성된 패키지
> - 소프트웨어를 설치, 관리하는 패키지 관리 시스템
> - Django = pip 패키지

- 장고 프로젝트 생성

```
django-admin startproject <장고프로젝트이름>
```

- 장고 프로젝트로 이동

```
cd <장고프로젝트이름>
```

- manage.py로 서버 작동

> 장고 프로젝트 생성시 manage.py라는 파일이 있는데
>
> 이 파이썬 파일로 서버로 돌린다.

```
python manage.py runserver
```

- App 생성하기

> django에서 App이란?
>
> 프로젝트의 구성단위이며 이 앱들이 모여 프로젝트를 이룬다.
>
> 예를들어 
>
> - 로그인 기능을 정의한 loginapp
>
> - 블로그 기능을 정의한 blogapp
>
> 등 기능별로 앱을 분리하여 관리한다.

```
python manage.py startapp <앱이름>
```

- 장고프로젝트에게 app이 생성되었다고 알리기 (settings.py)

> 장고프로젝트 안에서 앱을 생성하면 장고프로젝트의 settings.py에 앱을 등록함으로써
>
> 앱이 생성된 것을 입력해야한다.

```python
#(settings.py)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  	'<앱이름>.apps.<(첫글자대문자)앱이름>Config' ##예) wordcountapp.apps.WordcountappConfig
]

```

- 한국시간, 한글로 환경설정

```python
# (settings.py)

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'asia/seoul'
```

- 앱 폴더에 유저에게 보여질 화면을 담을 templets폴더 생성하기

> 장고프로젝트에서는 각 앱에서 유저에게 보여질 화면, 즉 html을 담을 폴더인 templates 폴더를 생서해야한다.

- 어드민 계정 생성

```python 
python manage.py createsuperuser
```

- models.py에서 모델 정의후 DB등록

```python
python manage.py makemigrations
pyrhon manage.py migrate
```

- admin에 모델 등록하기

```python
# (admin.py)
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)
```

