from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from interfaces.api.urls import urlpatterns as api_urls
from interfaces.front.urls import urlpatterns as front_urls


urlpatterns = (
    [
        path('admin/', admin.site.urls),
    ]
    + api_urls
    + front_urls
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

