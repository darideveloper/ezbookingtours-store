from django.urls import path
from ashley_jonathan import views

urlpatterns = [
    path("sale/", views.SaleView.as_view(), name="sales"),
    path("sale/<int:sale_id>/", views.SaleDoneView.as_view(), name="sale_detail"),
]
