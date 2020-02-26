from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', include('project_apps.dashboard.urls'), name='home'),
    path('auth', include('project_apps.authenticate.urls')),
    path(r'api', include('project_apps.api.urls')),
    path('error', include('project_apps.errors.urls')),
    url(r'^byte-map/', admin.site.urls)
]
if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

