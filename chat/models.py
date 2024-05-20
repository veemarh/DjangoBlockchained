from django.db import models

from accounts.models import User, Teacher, Student


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='room_teacher')
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='room_student')

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name} - {self.slug}"


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    body = models.TextField()
    sent_by = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.sent_by},"
