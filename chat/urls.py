from django.urls import path

from . import views

urlpatterns = [
#    path("", views.ChatRoomView.as_view(template_name="chat_room.html"), name="chat_room"),
    path("<slug:slug>/", views.room, name='room'),
]