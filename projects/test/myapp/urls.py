from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name = 'list'),
    path('create/<int:pk>', views.BlogDetail.as_view(), name = 'detail'),
    path('create/', views.BlogCreate.as_view(), name = 'create'),
    path('update/<int:pk>/', views.BlogUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name = 'delete'),
]
