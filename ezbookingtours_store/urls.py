from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('store/', include('store.urls'))
]
