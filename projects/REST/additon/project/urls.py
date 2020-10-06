from django.contrib import admin
from django.urls import path, include
from rest_framework import urls # api 서버 html 내부에 로그인 구현하기위함.
from rest_framework.authtoken.views import obtain_auth_token # 발급한 토큰 획득하기

urlpatterns = [
    path('admin/', admin.site.urls),
    # 서버클라이언트 화면에 로그인창 구현
    # 주의점은 authentication dl BasicAuthentication으로 설정하면 안되다. Token 방식은 가능! 
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('post/', include('post.urls')),
    path('userpost/', include('userpost.urls')),
]
