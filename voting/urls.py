from django.contrib import admin
from django.urls import path, re_path as url, include
from django.conf import settings
import votes.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(votes.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


