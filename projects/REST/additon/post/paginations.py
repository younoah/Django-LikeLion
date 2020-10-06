from rest_framework.pagination import PageNumberPagination

# 커스터마이즈 페이지네이션 구현
class MyPagination(PageNumberPagination):
    page_size = 5