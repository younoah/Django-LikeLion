# 데이터 처리 대상 : 모델, Serializer import 시키기
from post.models import Post
from post.serializers import PostSerializer

from rest_framework import viewsets
from post.paginations import MyPagination

# @action처리
from rest_framework.decorators import action
from rest_framework import renderers
from django.http import HttpResponse

# ReadOnlyModelViewSet과 ModelViewSet 하나만 사용
# CRUD가 가능한 ModelViewSet을 사용하자.

# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능
# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# ModelViewSet은 ListView와 DetailViewdㅔ 대한 CRUD가 모두 가능
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()#.order_by('id')
    serializer_class = PostSerializer
    pagination_class = MyPagination

    # @acitons(method=['post'])로 하면 POST로 호출하게된다.
    # 아래는 method= 인자가 생략 되었기 떄문에 default 값인 GET으로 세팅되었다.
    @action(detail=True, renderer_classes = [renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def highlight(self, req, *args, **kwargs):
        return HttpResponse("얍")

# 페이지네이션을 할 떄에는 반드시 레코드를 정렬한 상태에서 페이지네이션을 수행할 것
# 정렬를 정의하지 않으면 페이지네이션을 할떄 글 순서가 아무 기준 없이 섞일수도 있다.
# 정렬 방법은 크게 2가지가 있다.
# 1. view의 클래스에서 쿼리셋에 모델.objects.all().order_by('정렬기준') (정렬기준: 모델 필드)
# 2. models.py에서 메타 클래스를 활용한다.
# # pug_date 역순으로 정렬
# ordering = ['-pub_date']
# # 무작위 정렬
# ordering = ['?']
# # pub_date를 내림차순으로 정렬한 후, author를 오름차순으로 정렬
# ordering = ['-pub_date', 'author']
# # 쿼리식도 사용가능
# # author을 오름차순으로 정렬하고 null 값을 마지막으로 정렬
# ordering = [F('author').asc(nulls_last=True)]
# # umber 필드를 내림차순으로 정렬하고 
# # price 필드를 오름차순으로 정렬
# ordering = ['-number', 'price']