from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_urls
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from apps.servicos import urls as servicos_urls
from apps.ronda import urls as ronda_urls
from apps.gerador_qrcode import urls as qr_url
from apps.apontamento import urls as apontamento_url

from django.conf import settings


urlpatterns = [
    path('apontamento/', include(apontamento_url)),
    path('qr/', include(qr_url)),
    path('dashboard/', include(ronda_urls)),
    path('servicos/',  include(servicos_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',  include(home_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )



