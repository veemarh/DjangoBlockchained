from django.views.generic import CreateView

from .models import Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ["name", "description", "price", "duration"]
    template_name = "create_service.html"

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teacher
        return super().form_valid(form)
