from django.contrib import admin
from django.urls import path
# import blogapp.views 라고 작성해도된다.
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name = 'detail'),
    path('new', views.new, name = 'new'),
    path('create', views.create, name = 'create'),
]