import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('pages.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('home/', include('home.urls')),
    path('owners/', include('owners.urls')),
    path('properties/', include('properties.urls')),
    path('renters/', include('renters.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
