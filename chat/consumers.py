from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        group = self.scope["url_route"]["kwargs"]["group"]
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)
        
    def disconnect(self, code):
        self.disconnect()
        group = self.scope["url_route"]["kwargs"]["group"]
        async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
    
    def receive(self, text_data):
        group = self.scope["url_route"]["kwargs"]["group"]
        message = json.loads(text_data)["message"]

        async_to_sync(self.channel_layer.group_send)(group, {
            "type":"chat.message",
            "msg":message
        })
    
    def chat_message(self, event):
        message = event["msg"]
        self.send(text_data=json.dumps({"message":message}))

