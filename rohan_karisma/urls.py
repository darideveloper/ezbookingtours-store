from rohan_karisma import views
from django.urls import path

urlpatterns = [
    path('sale/', views.SaleView.as_view(), name='sales'),
]