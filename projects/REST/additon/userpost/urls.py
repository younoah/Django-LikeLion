from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userpost import views

# 라우터가 없다면?

router = DefaultRouter()
router.register('', views.UserPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]