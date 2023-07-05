from wedding import views
from django.urls import path

urlpatterns = [
    path ('', views.IndexView.as_view(), name="index"),
    path ('validate-vip-code/', views.ValidateVipCodeView.as_view(), name='validate_vip_code'),
    path ('buy/', views.BuyView.as_view(), name='buy'),
]