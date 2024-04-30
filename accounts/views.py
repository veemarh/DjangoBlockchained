from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView

from .decorators import student_required
from .forms import (
    StudentCreationForm,
    TeacherCreationForm,
    InterestsChangeForm,
)
from .models import User, Student


class SignUpView(TemplateView):
    template_name = "registration/signup.html"


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentCreationForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


@method_decorator([login_required, student_required], name="dispatch")
class StudentInterestsUpdateView(UpdateView):
    model = Student
    form_class = InterestsChangeForm
    template_name = "registration/interests_form.html"

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, "Interests updated with success!")
        return super().form_valid(form)


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherCreationForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "teacher"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("")


class StudentProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = "student_profile.html"

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user


class StudentProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = (
        "username",
        "first_name",
        "second_name",
        "third_name",
        "birth_date",
        "phone_number",
        "email",
    )
    template_name = "student_profile_edit.html"

    success_url = ".."

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user
