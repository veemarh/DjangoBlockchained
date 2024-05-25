from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView

from accounts.models import Teacher, Subject
from .utils import q_search


class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teachers"  # Optional: custom name for context
    template_name = "teacher_list.html"

    def get_context_data(self, *args, **kwargs):
        kwargs["interests"] = [subject.name for subject in list(Subject.objects.all())]
        # print([subject.name for subject in list(Subject.objects.all())])
        return super().get_context_data(**kwargs)


def catalog(request, category_slug=None):
    page = request.GET.get("page")
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        teachers = Teacher.objects.all()
    elif query:
        teachers = q_search(query)
    else:
        teachers = get_list_or_404(Teacher.objects.filter(category_slug=category_slug))

    if order_by and order_by != "default":
        teachers = teachers.order_by(order_by)

    paginator = Paginator(teachers, 4)
    current_page = paginator.page(int(page))

    context = {
        "teachers": current_page,
        "slug_url": category_slug,
    }
    return render(request, "teacher_list.html", context)
