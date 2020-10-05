# 데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer
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



# class PostVeiwSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer