from . import views
from django.urls import path

app_name = "store"
urlpatterns = [
    path ('', views.index, name="index"),
    # path ('keagan/', views.keagan_home, name="keagan_home"),
    # path ('keagan/category-products/<str:brand_name>/', views.keagan_category_products, name="keagan_category_products"),
    # path ('keagan/payment/', views.keagan_payment, name="keagan_payment")
]