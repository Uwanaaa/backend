"""
ASGI config for dalensai project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter,ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from django.core.asgi import get_asgi_application



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dalensai.settings')

application = get_asgi_application()


from home.stream import Streams

websocket_urlpatterns = [
    path('feed/',Streams.as_asgi())
]

application = ProtocolTypeRouter ({
    'http': application,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    )
    )
})                                                                                                                   