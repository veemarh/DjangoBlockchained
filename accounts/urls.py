from django.urls import path
from django.views.generic import TemplateView

from .views import (
    StudentProfileView,
    StudentProfileUpdateView,
    StudentInterestsView,
    TeacherProfileView,
    TeacherProfileUpdateView,
)

urlpatterns = (
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "student/interests/",
        StudentInterestsView.as_view(),
        name="student_interests",
    ),
    path(
        "student/profile/<int:pk>/",
        StudentProfileView.as_view(),
        name="student_profile",
    ),
    path(
        "student/profile/<int:pk>/edit/",
        StudentProfileUpdateView.as_view(),
        name="student_profile_edit",
    ),
    path(
        "teacher/profile/<int:pk>/",
        TeacherProfileView.as_view(),
        name="teacher_profile",
    ),
    path(
        "teacher/profile/<int:pk>/edit",
        TeacherProfileUpdateView.as_view(),
        name="teacher_profile_edit",
    ),
)
