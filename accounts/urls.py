from django.urls import path, include
from django.views.generic import TemplateView

from .views import StudentSignUpView, TeacherSignUpView, StudentInterestsView

urlpatterns = [
    path("students/", TemplateView.as_view(template_name="home.html"), name="home"),
    path("teacher/", TemplateView.as_view(template_name="home.html"), name="home"),
    path("students/interests/", StudentInterestsView.as_view(), name="interests"),
]
