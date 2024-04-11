from django.contrib.auth.models import AbstractUser
from django.db import models


class StudentUser(AbstractUser):
    first_name = models.CharField(max_length=15, null=False, blank=False)
    second_name = models.CharField(max_length=15, null=False, blank=False)
    third_name = models.CharField(max_length=15, null=True, blank=True)
    school_name = models.CharField(max_length=20, null=True, blank=True)
    # age = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField()


class TeacherUser(AbstractUser):
    first_name = models.CharField(max_length=15, null=False, blank=False)
    second_name = models.CharField(max_length=15, null=False, blank=False)
    third_name = models.CharField(max_length=15, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField()
    birth_date = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=30)
    # certificates = models.Li Пока не разобрался как тут сделать список
    # subjects
    # и так далее
