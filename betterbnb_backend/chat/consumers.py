import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import ConversationMessage

from useraccount.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        print(f"Received data: {data}")
        
        Conversation_id = data['data']['conversation_id']
        receiver_id = data['data']['receiver']
        name = data['data']['name']
        body = data['data']['body']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'body': body,
                'name': name
            }
        )

        await self.save_message(Conversation_id, body, receiver_id)

    async def chat_message(self, event):
        body = event['body']
        name = event['name']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'body': body,
            'name': name,
        })) 

    
    @sync_to_async
    def save_message(self, conversation_id, body, receiver_id):
        user = self.scope['user']

        self.receiver = User.objects.get(pk=receiver_id)

        ConversationMessage.objects.create(
            conversation_id=conversation_id,
            body=body,
            sender=user,
            receiver=self.receiver
        )
        