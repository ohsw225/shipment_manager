from django.contrib.auth.models import AbstractBaseUser
from django.http import HttpRequest


def has_owner_or_staff_permission(request: HttpRequest, owner: AbstractBaseUser | None) -> bool:
    """Return True if the request user is staff or matches the owner."""
    user = request.user
    if not user.is_authenticated:
        return False
    if user.is_staff:
        return True
    return owner is not None and owner == user
