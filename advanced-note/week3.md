## DRF의 View

강의 자료 : https://www.django-rest-framework.org/

### ViewSet

- view(CRUD)를 설계하는 쉽고 간단한 방법



### View를 배우는 과정 - ViewSet에 이르는과정

> 코드복잡도는 상위일수록 복잡하다. 즉, ViewSet이 과정 간단하다.
>
> 위에서부터 아래로 상속하면서 만들어진 형태라 위에서부터 차근차근 알면 좋다.

1. APIView
2. Mixins
3. Generic CBV
4. ViewSet

### 

## APIVeiw

> APIView를 상속하여 View를 설계할 땐 `status` 와 `Response` 를 import해와서 직접 **응답**과정을 만든다.
>
> 장점으로는 직접 응답을 짜기 때문에 개발자 입맛대로 정의할수 있다.
>
> 단점으로 왠만한 모델은 리스트, 디테일,  get, post, put, delete 동작이 똑같이 필요한데 매번 일일히 정의하는게 불편하다.



### models.py

```python
from django.db import models

class Post(models.Model):
    objects = models.Manager() #  class has no objects member 에러 예방
    title = models.CharField(max_length = 50)
    body = models.TextField()
```



### serializers.py

```python
from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['title', 'body'] 모델의 타이틀과 바디 필드만 채용
        fields = '__all__' 
```



### views.py

```python
# 데이터 처리 대상
from post.models import Post
from post.serializers import PostSerializer
# status에 따라 직접 Response를 처리할 것
from django.http import Http404 # Get Ovbject or 404 직접 구현
from rest_framework.response import Response
from rest_framework import status
# APIView를 상속받은 CBV
from rest_framework.views import APIView
# PostDetail 클래스의 get_object 메서드 대신 이거 써도된다.
# from django.shortcuts import get_object_or_404

class PostList(APIView):
    def get(self, req):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True) # 쿼리셋 넘기기, 다수의 쿼리셋을 직렬화할 땐 꼭 many = True해야한다.
        return Response(serializer.data) # 직접 Response 리턴해주기 : serializer.data

    def post(self, req):
        serializer = PostSerializer(data = req.data)
        if serializer.is_valid(): # 직접 유효성 검사
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

# PostList 클래스와는 달리 pk값을 받는다. (메서드에 pk인자)
class PostDetail(APIView):
    # get_object_or_404를 구현해주는 helper function
    def get_object(self, pk):
        try:
            return Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, req, pk, fromat = None):
        post = self.get_object(pk)
        # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # 위 post 메서드와 비슷비슷한 논리
    def put(self, req, pk, format = None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data = req.data)

    def delete(self, req, pk, format = None):
        post = self.get_object(pk)
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
```



### urls.py

```python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

# Default Router 사용안함 => APi ROOT 없음.

# router = DefaultRouter()
# router.register('post', views.PostVeiwSet)

urlpatterns = [
    # 127.0.0.1:8000/post == ListView
    path('post/', views.PostList.as_view()),
    # 127.0.0.1:8000/post == DetailView
    path('post/<int:pk>', views.PostDetail.as_view()),
]

#
urlpatterns = format_suffix_patterns(urlpatterns)
```





## mixins

> APIView에서 list, detail 등의 클래스와 get, put, post 등의 메서드의 재사용성을 위해 상속을 활요하여 좀더 편리하게 사용한다.



### models.py (위와 동일)

```python
from django.db import models

class Post(models.Model):
    objects = models.Manager() #  class has no objects member 에러 예방
    title = models.CharField(max_length = 50)
    body = models.TextField()
```



### serializers.py (위와 동일)

```python
from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['title', 'body'] 모델의 타이틀과 바디 필드만 채용
        fields = '__all__' 
```



### views.py

```python
# 데이터 처리 대상 : 모델, Serializer import 시키기
from post.models import Post
from post.serializers import PostSerializer

from rest_framework import generics
from rest_framework import mixins


class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all() # 쿼리셋 등록
    serializer_class = PostSerializer # Serializer 클래스 등록

    # get은 list 메서드를 내보내는 메서드
    def get(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

    # post는 create을 내보내는 메서드
    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)


class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all() # 쿼리셋 등록
    serializer_class = PostSerializer # Serializer 클래스 등록

    # DetailView의 get은 retrieve을 내보내는 메서드
    def get(self, req, *args, **kwargs):
        return self.retrieve(req, *args, **kwargs)

    # put은 update을 내보내는 메서드
    def put(self, req, *args, **kwargs):
        return self.update(req, *args, **kwargs)
    
    # delet는 destroy를 내보내는 메서드
    def delete(self, req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)
```



### urls.py (위와 동일)

```python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

# Default Router 사용안함 => APi ROOT 없음.

# router = DefaultRouter()
# router.register('post', views.PostVeiwSet)

urlpatterns = [
    # 127.0.0.1:8000/post == ListView
    path('post/', views.PostList.as_view()),
    # 127.0.0.1:8000/post == DetailView
    path('post/<int:pk>/', views.PostDetail.as_view()),
]

#
urlpatterns = format_suffix_patterns(urlpatterns)
```



