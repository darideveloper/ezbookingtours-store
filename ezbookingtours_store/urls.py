from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('riviera/', include('riviera_maya_airport_transfers.urls')),
    path('wedding/', include('wedding.urls')),
]

handler404 = 'store.views.error_404'
