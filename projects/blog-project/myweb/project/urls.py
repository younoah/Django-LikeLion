from django.contrib import admin
from django.urls import path
from django.urls import path, include
# import homeapp.views
# import blogapp.views
import portfolioapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeapp.urls')),
    path('blog/', include('blogapp.urls')),
    path('portfolio/', portfolioapp.views.portfolio, name = 'portfolio'),
]
