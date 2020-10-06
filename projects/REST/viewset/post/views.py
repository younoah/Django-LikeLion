# 데이터 처리 대상 : 모델, Serializer import 시키기
from post.models import Post
from post.serializers import PostSerializer

from rest_framework import viewsets

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
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @acitons(method=['post'])로 하면 POST로 호출하게된다.
    # 아래는 method= 인자가 생략 되었기 떄문에 default 값인 GET으로 세팅되었다.
    @action(detail=True, renderer_classes = [renderers.StaticHTMLRenderer])
    # 그냥 얍을 띄우는 custom api
    def highlight(self, req, *args, **kwargs):
        return HttpResponse("얍")

