from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolioapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name = 'home'),
    path('blog/', include('blogapp.urls')),
    path('portfolio', portfolioapp.views.portfolio, name = 'portfolio'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  