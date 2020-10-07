from django.contrib import admin
from django.urls import path, include
import funccrud.views
import funccrud.urls
import classcrud.views
import classcrud.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('func-blog/', include('funccrud.urls')),
    path('class-blog/', include('classcrud.urls')),
]
