from django.db import models
from django.urls import reverse

from accounts.models import Teacher


class Service(models.Model):
    # Услуга, которую оказывает препод
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    duration = models.DurationField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("teacher_services")
