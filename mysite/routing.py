from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_url_patterns
from django.urls import path
from chat.models import Group
from django.contrib.auth.models import User

list(map(User.delete, User.objects.all()))
list(map(Group.delete, Group.objects.all()))

application = ProtocolTypeRouter({
    "websocket":URLRouter(websocket_url_patterns)
})