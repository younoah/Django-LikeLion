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
