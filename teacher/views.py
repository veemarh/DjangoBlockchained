from django.shortcuts import render
from accounts.models import Teacher
from django.views.generic import ListView


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teachers'  # Optional: custom name for context
    template_name = "teacher_list.html"
    queryset = Teacher.objects.all()

