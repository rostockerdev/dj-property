from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Errors
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path("dev/", admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('realtors/', include('realtors.urls', namespace='realtors')),
]

handler400 = "core.views.bad_request"
handler403 = "core.views.permission_denied"
handler404 = "core.views.not_found"
handler500 = "core.views.server_error"

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
