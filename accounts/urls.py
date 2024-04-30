from django.urls import path
from django.views.generic import TemplateView

from .views import (
    StudentInterestsView,
    StudentProfileView,
    StudentProfileUpdateView,
    StudentInterestsEditView,
)

urlpatterns = (
    path("student/", TemplateView.as_view(template_name="home.html"), name="home"),
    path("teacher/", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "student/<int:pk>/interests/",
        StudentInterestsView.as_view(),
        name="interests",
    ),
    path(
        "student/<int:pk>/interests/edit/",
        StudentInterestsEditView.as_view(),
        name="interests_edit",
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
)
