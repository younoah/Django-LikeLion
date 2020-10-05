from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['title', 'body'] 모델의 타이틀과 바디 필드만 채용
        fields = '__all__' 
