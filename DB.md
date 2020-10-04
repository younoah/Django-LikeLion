> 참고자료
>
> https://ossian.tistory.com/95



1. mysql 모듈 패키지 설치

```
pip install Django mysqlclient
```

2. settings.py에서 DATABASE 부분 수정

```python
DATABASES = {
  ‘default’: {
    # 기존 설정, 지우기
    #'ENGINE': 'django.db.backends.sqlite3',
    #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    ‘ENGINE’: ‘django.db.backends.mysql’, # mysql 엔진 설정
    ‘NAME’: ‘myproject’, # 데이터 베이스 이름
    ‘USER’:’DB에 접속할때 설정한 이름’, # 데이터베이스 연결 시 사용할 계정
    ‘PASSWORD’:’DB에 접속할때 설정한 비밀번호', # 계정 비밀번호
    ‘HOST’:’localhost’, # 데이터베이서 서버 IP
    ‘PORT’:’’, # MySQL 연결 옵션 설정
    # 아래는 옵션인데 작성안해도 무방한듯
    'OPTIONS': {
              'charset' : 'utf8',
              'use_unicode' : True,
               'init_command': 'SET '
                  'storage_engine=INNODB,'
                  'character_set_connection=utf8,'
                  'collation_connection=utf8_bin'
                  #'sql_mode=STRICT_TRANS_TABLES,'    # see note below
                  #'SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
    },
  }
}

```

