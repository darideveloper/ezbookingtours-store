from . import views
from django.urls import path
from django.contrib import admin

admin.site.site_header = "Ezbookingtours Store"
admin.site.site_title = 'Ezbookingtours Store'
admin.site.site_url = 'https://ezbookingtours.com'
admin.site.index_title = "Admin"


urlpatterns = [
    path ('', views.index, name="index"),
    # path ('keagan/', views.keagan_home, name="keagan_home"),
    # path ('keagan/category-products/<str:brand_name>/', views.keagan_category_products, name="keagan_category_products"),
    # path ('keagan/payment/', views.keagan_payment, name="keagan_payment")
]