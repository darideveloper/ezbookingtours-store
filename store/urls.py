from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("widget/<str:location>/<str:tour>/", views.widget, name="widget"),
    path("success/<int:sale_id>/", views.success, name="success"),
    path("404/", views.error_404_view, name="error_404"),
    path("test-email/", views.test_email, name="test_email"),
]
