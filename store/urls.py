from . import views
from django.urls import path
from django.contrib import admin

admin.site.site_header = "Ezbookingtours Store"
admin.site.site_title = 'Ezbookingtours Store'
admin.site.site_url = 'https://ezbookingtours.com'
admin.site.index_title = "Admin"

app_name = "store"

urlpatterns = [
    path ('', views.index, name="index"),
    path ('widget/<str:location>/<str:tour>/', views.widget, name='widget'),
    path ('success/<int:sale_id>/', views.success, name='success'),
]
    
    