from userpost.models import UserPost
from userpost.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter # 검색기능라이브러리

# 뷰단에서 따로 authentication 인증방식 설정, 뷰 개별적으로 적용하기 위함
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

# permisiion 뷰단 별로 설정을 위해 permission class들을 임포트
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


class UserPostViewSet(viewsets.ModelViewSet):
    # authentication 인증 방식 설정, 아래 같은 경우 BasicAuthentication, SessionAuthentication 2개를 채용
    authentication_classes = [TokenAuthentication]

    # 뷰에 permission 설정
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    ## 검색 ##
    # 어떤것을 기반으로 검색을 할지 지정
    filter_backends = [SearchFilter]
    # 어떤 컬럼을 기반으로 검색을 할 건지 (튜플)로 지정 
    search_fields = ('title','body') # 튜플의 인자가 1개일 때는 끝에 컴마를 찍어야한다.

    # 쿼리셋을 기반으로 어떤 조작을 할때에는 위의 queryset 변수에 직접 접근하지말고
    # 아래와같이 viewsets.ModelViewSet에 정의되어있는 get_queryset()메서드를 선언하여
    # 메서드 안에어 지지고 볶은 다음에 리턴하는 방식으로구현하자.
    def get_queryset(self):
        # 부모클래스(상위클래스)의 쿼리셋을 갖고온다. 이거 -> queryset = UserPost.objects.all()
        qs = super().get_queryset()
        # 쿼리셋의 필터링 메서드 : .filter, .exclude
        # qs = qs.filter(author__id = 1) # author의 id가 1번으로 필터링한다.

       # 지금 만약 로그인이 되어있다면 로그인한 유저의 글만 필터링해라
        if self.request.user.is_authenticated: 
            qs =  qs.filter(author = self.request.user)
         # 만약 로그인이 안되어있다면 비어있는 쿼리셋을 리턴해라
        else: 
            qs =  qs.none()
        return qs
    
    ## author_name 필드 ##
    # 시리얼라이저에 임의의 author_name이라는 필드를 생성했으니
    # 뷰에서 새로운 필드를 만들었으니 저장할때 같이 저장하라고 알려줘야한다.
    # 그래야 author_name도 저장이된다.

    # perform_create()메서드를 이용해서 저장한다.
    # self객체에 있는 (serializer) author_name을 같이 저장하기위함
    # serializer의 save()메서드를 통해서 autor필드에 지금 요청을 보낸 유저를 저장한다.
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)