from .models import UserPost
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    # author에 있는 username을 athor_name으로 삼고 읽기전용으로한다.
    # 리드온리는 특정 필드를 편집하지 못하게 오직 읽기 형식필드로 만든다.
    # 시리얼라이저에 임의의 author_name이라는 필드를 생성했으니
    # 뷰에서 새로운 필드를 만들었으니 저장할때 같이 저장하라고 알려줘야한다.
    # 그래야 author_name도 저장이된다.
    author_name = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = UserPost
        # fields = '__all__' 
        fields = ('pk', 'author_name', 'title', 'body')


    
