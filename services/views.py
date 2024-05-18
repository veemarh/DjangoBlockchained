from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .models import Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ["name", "description", "price", "duration"]
    template_name = "create_service.html"

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teacher
        return super().form_valid(form)


class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # new
    model = Service
    # template_name = "service_delete.html"
    success_url = reverse_lazy("teacher_services")

    def test_func(self):
        obj = self.get_object()
        return obj.teacher == self.request.user.teacher
