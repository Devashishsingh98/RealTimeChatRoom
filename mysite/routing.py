from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_url_patterns
from django.urls import path

application = ProtocolTypeRouter({
    "websocket":URLRouter(websocket_url_patterns)
})