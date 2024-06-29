from rohan_karisma import views
from django.urls import path

urlpatterns = [
    path('sale/', views.SaleView.as_view(), name='sales'),
    path('sale/<int:sale_id>/', views.SaleDoneView.as_view(), name='sale_detail'),
]