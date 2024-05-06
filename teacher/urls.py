from django.urls import path

from . import views

urlpatterns = [
    #path("", views.TeacherListView.as_view()),
    path("", views.TeacherListView.as_view(template_name="teacher_list.html"), name="teacher_list"),
    #path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
