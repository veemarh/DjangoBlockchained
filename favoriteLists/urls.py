from django.urls import path
from django.views.generic import TemplateView

# from .views import FavoriteTeachersListView

urlpatterns = (
    path(
        "teachers/",
        TemplateView.as_view(template_name="favorite_teachers.html"),
        name="favorite_teachers_list",
    ),
)
