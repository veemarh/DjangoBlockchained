from django.views.generic import ListView

from .models import Room


class ChatRoomView(ListView):
    model = Room
    context_object_name = "room"  # Optional: custom name for context
    template_name = "chat_room.html"
