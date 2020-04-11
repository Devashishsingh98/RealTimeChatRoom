from .consumers import ChatConsumer
from django.urls import path

websocket_url_patterns = [
    path("chat/<str:group>/", ChatConsumer)
]