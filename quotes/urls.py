from django.urls import path
from . import views

urlpatterns = [
    path("generate/", views.generate_quote, name="generate_quote"),
]
