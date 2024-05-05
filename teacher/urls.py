from django.urls import path

from . import views

urlpatterns = [
    path("", views.TeacherListView.as_view()),
]
