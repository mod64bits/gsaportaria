from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_urls
from django.conf.urls.static import static

from apps.servicos import urls as servicos_urls

from django.conf import settings


urlpatterns = [
    path('servicos/',  include(servicos_urls)),
    path('',  include(home_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )



