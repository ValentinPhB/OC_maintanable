from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

def trigger_error(request):
    division_by_zero = 1 / 0
    
urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='letting')),
    path('profiles/', include('profiles.urls', namespace='profile')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
