from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import home





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('mypage/', include('mypage.urls')),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)