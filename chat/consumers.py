from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import GroupMessage
import json

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        group = self.scope["url_route"]["kwargs"]["group"]

        if group not in list(map(str, list(GroupMessage.objects.all()))):
            new_group = GroupMessage(name=group, message="")
            new_group.save()

        else:
            g = GroupMessage.objects.get(name=group)
            self.send(text_data=json.dumps({"message":g.message}))

        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)
        
    def disconnect(self, code):
        self.close(code)
            
    def receive(self, text_data):
        group = self.scope["url_route"]["kwargs"]["group"]
        message = json.loads(text_data)["message"]
        
        g = GroupMessage.objects.get(name=group)
        g.message += message + "\n"
        g.save()

        async_to_sync(self.channel_layer.group_send)(group, {
            "type":"chat.message",
            "msg": GroupMessage.objects.get(name=group).message
        })
    
    def chat_message(self, event):
        message = event["msg"]
        self.send(text_data=json.dumps({"message":message}))

