from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default="#007bff")

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = (
            '<span class="badge badge-primary" style="background-color: %s">%s</span>'
            % (color, name)
        )
        return mark_safe(html)


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    first_name = models.CharField(max_length=15, null=False, blank=False)
    second_name = models.CharField(max_length=15, null=False, blank=False)
    third_name = models.CharField(max_length=15, null=True, blank=True)

    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Subject, related_name="interested_students")

    school_name = models.CharField(max_length=20, null=True, blank=True)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
