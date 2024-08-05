from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Omar Dashboard"
admin.site.site_title = 'Omar Dashboard'
admin.site.site_url = ''
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('riviera/', include('riviera_maya_airport_transfers.urls')),
    path('wedding/', include('wedding.urls')),
    path('will-ryan/', include('will_ryan_airport_transfers.urls')),
    path('rohan-karisma/', include('rohan_karisma.urls')),
    path('driven-mastermind/', include('driven_mastermind.urls')),
]

handler404 = 'store.views.error_404'
