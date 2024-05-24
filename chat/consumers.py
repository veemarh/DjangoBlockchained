import json

from asgiref.sync import sync_to_async
# talk to database
# consumer or web socket
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timesince import timesince

from accounts.models import User
from chat.models import Room, Message
from chatextras import initials


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_layer
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_layer
        )

    async def receive(self, text_data):
        # Receive message from WebSocket (frontend)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        room = text_data_json["room"]

        await self.save_message(username, room, message)
        new_message = await self.create_message(username, room, message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'initials': initials(username),
                'created_at': timesince(new_message.created_at),
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "type": "chat_message",
                    "message": event["message"],
                    "username": event["username"],
                    "initials": event["name"],
                    "created_at": event["created_at"],
                }
            )
        )

    def create_message(self, username, room, message):
        message = Message.objects.create(body=message, username=username, room=room)
        self.room.message.add(message)

        return message

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, body=message)
