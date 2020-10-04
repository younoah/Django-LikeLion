from django.contrib import admin
from django.urls import path, include
import myapp.views
import myapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name = 'home'),
    path('blog', include(myapp.urls)),

]
