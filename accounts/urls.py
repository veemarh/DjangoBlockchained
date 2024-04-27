from django.urls import path
from django.views.generic import TemplateView

from .views import (
    StudentInterestsUpdateView,
    StudentProfileView,
    StudentProfileUpdateView,
)

urlpatterns = [
    path("student/", TemplateView.as_view(template_name="home.html"), name="home"),
    path("teacher/", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "student/<int:pk>/interests/",
        StudentInterestsUpdateView.as_view(),
        name="interests",
    ),
    path(
        "student/profile/<int:pk>/",
        StudentProfileView.as_view(),
        name="student_profile",
    ),
    path("student/profile/<int:pk>/edit/", StudentProfileUpdateView.as_view()),
]
