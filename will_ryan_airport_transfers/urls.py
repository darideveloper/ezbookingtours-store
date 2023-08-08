from . import views
from django.urls import path

urlpatterns = [
    path ('', views.index, name="index"),
    path ('hotels/', views.hotels, name='hotels'),
    path ('transports/', views.transports, name='transport'),
]