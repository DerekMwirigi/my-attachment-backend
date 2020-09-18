from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/', include('project_apps.api.urls')),
    path('api/v1/', include('project_apps.services.aftlkng_api.urls')),
    url('admin/', admin.site.urls)
]
if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

