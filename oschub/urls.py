from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
    path('main/', include('main.urls')),
    path('eventreg/', include('eventreg.urls')),
    path('livestream/', include('livestreams.urls')),
]
