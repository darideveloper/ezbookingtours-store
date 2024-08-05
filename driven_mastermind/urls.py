from driven_mastermind import views
from django.urls import path

urlpatterns = [
    path('sale/', views.SaleView.as_view(), name='sales'),
]