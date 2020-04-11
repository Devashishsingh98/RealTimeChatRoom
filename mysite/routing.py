from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_url_patterns
from django.urls import path
from chat.models import GroupMessage

list(map(GroupMessage.delete, GroupMessage.objects.all()))

application = ProtocolTypeRouter({
    "websocket":URLRouter(websocket_url_patterns)
})