from django.contrib import admin
from django.urls import path
import wordcountapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcountapp.views.index, name = "index"),
    path('about/',wordcountapp.views.about, name = "about"),
    path('result/',wordcountapp.views.result, name = "result"),
]
