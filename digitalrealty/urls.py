from digitalrealty import views
from django.urls import path

urlpatterns = [
    path("sale/", views.SaleView.as_view(), name="digitalrealty_sales"),
    path(
        "sale/<int:sale_id>/",
        views.SaleDoneView.as_view(),
        name="digitalrealty_sale_detail",
    ),
]
