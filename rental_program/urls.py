import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('pages.urls', namespace='pages')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('home/', include('home.urls', namespace='home')),
    path('renters/', include('renters.urls', namespace='renters')),
    path('owners/', include('owners.urls', namespace='owners')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
