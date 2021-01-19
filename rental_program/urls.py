from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('pages.urls')),
    path('accounts', include('accounts.urls')),
    path('owners/', include('owners.urls')),
    path('properties/', include('properties.urls')),
    path('renters/', include('renters.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
