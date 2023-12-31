from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('api/', include('api.urls', namespace='api')),
    path('rooms/', include('rooms.urls', namespace='rooms')),
    path('', home_view, name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
