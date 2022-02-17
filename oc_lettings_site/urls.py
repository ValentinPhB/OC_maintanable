from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='letting')),
    path('profiles/', include('profiles.urls', namespace='profile')),
    path('admin/', admin.site.urls),
]
