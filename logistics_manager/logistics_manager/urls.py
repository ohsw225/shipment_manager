from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from shipments.views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("admin/", admin.site.urls),
    path("shipments/", include("shipments.urls")),
    path("quotes/", include("quotes.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("healthz/", RedirectView.as_view(url="/")),
]
