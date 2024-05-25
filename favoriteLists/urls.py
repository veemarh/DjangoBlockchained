from django.urls import path

from .views import getFavoriteTeachersList, getFavoriteStudentsList

urlpatterns = (
    path(
        "teachers/",
        getFavoriteTeachersList,
        name="favorite_teachers_list",
    ),
    path(
        "student/",
        getFavoriteStudentsList,
        name="favorite_students_list",
    ),
)
