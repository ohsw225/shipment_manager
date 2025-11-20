from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("kr/", views.korea_shipments_view, name="shipments_kr"),
    path("au/", views.australia_shipments_view, name="shipments_au"),
    path("my/", views.my_shipments_view, name="my_shipments"),
]
