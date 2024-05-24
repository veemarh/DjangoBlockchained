from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from accounts.models import User
from .models import Room, Message


@require_POST
def create_room(request, slug):
    name = request.POST.get('name', '')
    slug = request.POST.get('slug', '')

    Room.objects.create(name=name, slug=slug)
    return JsonResponse({'message': 'Room created'})


@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, "rooms.html", {
        "rooms": rooms
    })

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    all_messages = Message.objects.filter(room=room)
    return render(request, 'chat_room.html', {
        'room': room,
        'all_messages': all_messages,
    })


@login_required
def delete_room(request, slug):
    room = Room.objects.get(slug=slug)
    room.delete()
    messages.success(request, 'You have successfully deleted this room.')
    return redirect('home')


class ChatRoomView(ListView):
    model = Room
    context_object_name = "room"  # Optional: custom name for context
    template_name = "chat_room.html"