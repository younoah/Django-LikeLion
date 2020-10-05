from django.contrib import admin
from django.urls import path, include
import post.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')), # 따옴표 없이 include(post.urls)로 써도 무방하다.
]
