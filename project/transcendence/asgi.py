"""
ASGI config for transcendence project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import docu.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transcendence.settings')

asgi_application = get_asgi_application() #new

application = ProtocolTypeRouter({
"http": asgi_application,
"websocket": 
    # AllowedHostsOriginValidator(
        # AuthMiddlewareStack(
            URLRouter(docu.routing.websocket_urlpatterns) 
        # )
    # ,)
})