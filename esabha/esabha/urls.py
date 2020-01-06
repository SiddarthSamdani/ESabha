from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('social/', include('social.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', RedirectView.as_view(url='social')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)