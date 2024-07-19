from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape
from django.utils.html import mark_safe


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

    first_name = models.CharField(max_length=15, null=True, blank=True)
    second_name = models.CharField(max_length=15, null=True, blank=True)
    third_name = models.CharField(max_length=15, null=True, blank=True)

    picture = models.ImageField(upload_to="profile_images/", default="default.jpg")
    # picture = models.ImageField(upload_to="profile_images/", blank=True)

    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField()

    def is_complete(self):
        is_user_fields_complete = (
            self.first_name
            and self.second_name
            and self.picture
            and (self.phone_number or self.email)
        )

        if self.is_teacher:
            return is_user_fields_complete and self.teacher.is_complete()
        return is_user_fields_complete


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(null=True, blank=True)
    interests = models.ManyToManyField(Subject, related_name="interests_teacher")

    diploma = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    favorite_students = models.ManyToManyField(User, related_name="favorite_students")

    def __str__(self):
        return self.user.username

    def is_complete(self):
        return self.diploma and self.experience and self.interests and self.description


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Subject, related_name="interests_student")

    school_name = models.CharField(max_length=20, null=True, blank=True)
    favorite_teachers = models.ManyToManyField(
        Teacher, related_name="favorite_teachers"
    )

    def __str__(self):
        return self.user.username

    def is_complete(self):
        return self.interests and self.school_name


# Teacher.__annotations__["favorite_students"] =  models.ManyToManyField(
#     Student, related_name="favorite_students"
# )

# print(Teacher.__dict__)
