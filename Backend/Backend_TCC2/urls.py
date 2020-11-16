from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from Tdados import urls as Tdados_urls


urlpatterns = [
    path('api/', include(Tdados_urls)),
    path('admin/', admin.site.urls),
]
