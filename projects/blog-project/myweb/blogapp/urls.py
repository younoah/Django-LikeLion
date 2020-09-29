from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.blog_list, name = 'blog_list'),
    path('detail/<int:blog_id>', views.blog_detail, name = 'blog_detail'),
    path('write', views.blog_write, name = 'blog_write'),
    path('create', views.create_blog, name = 'create_blog'),
    path('detail/<int:blog_id>/modify', views.blog_modify, name = 'blog_modify'),
    path('update/<int:blog_id>', views.update_blog, name = 'update_blog'),
    path('delete/<int:blog_id>', views.delete_blog, name = 'delete_blog'),
]
