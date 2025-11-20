"""
ASGI config for logistics_manager project.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "logistics_manager.settings.local")

application = get_asgi_application()
