from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Поле для log in и sign in Джанго нам предоставляет
# А вот sign up приходится писать ручками)))

# В будущем (возможно в крайне близком) мы перейдем customUser и достаточно большую
# часть бекенда (и фронта гы) для регистрации придется переписывать, но пока норм
