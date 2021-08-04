from django.contrib import admin
from django.urls import path

# Errors
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path("dev/", admin.site.urls),
]

handler400 = "core.views.bad_request"
handler403 = "core.views.permission_denied"
handler404 = "core.views.not_found"
handler500 = "core.views.server_error"
