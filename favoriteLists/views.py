# from django.views.generic import ListView
#
# from accounts.models import Teacher, Student
#
#
# # class FavoriteTeachersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
# class FavoriteTeachersListView(ListView):
#     model = Student
#     template_name = "favorite_teachers.html"
#
#     def get_queryset(self):
#         # return Teacher.objects.filter(
#         #     self.request.user.student.favorite_teachers
#         # )  # эммммм
#
