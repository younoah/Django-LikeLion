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