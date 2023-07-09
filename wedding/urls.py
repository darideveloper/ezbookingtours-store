from wedding import views
from django.urls import path

urlpatterns = [
    path ('', views.IndexView.as_view(), name="index"),
    path ('validate-vip-code/', views.ValidateVipCodeView.as_view(), name='validate_vip_code'),
    path ('buy/', views.BuyView.as_view(), name='buy'),
    path ('transports/', views.TransportsView.as_view(), name='transports'),
    path ('hotels/', views.HotelsView.as_view(), name='hotels'),
    path ('free-dates/', views.FreeDatesView.as_view(), name='free'),
    path ('success/<int:sale_id>/', views.SuccessView.as_view(), name='success'),
] 