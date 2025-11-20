from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Dashboard placeholder")


@login_required
def korea_shipments_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Korea shipments placeholder")


@login_required
def australia_shipments_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Australia shipments placeholder")


@login_required
def my_shipments_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("My shipments placeholder")
