from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    TemplateView,
    DetailView,
)

from .forms import (
    StudentCreationForm,
    TeacherCreationForm,
    StudentInterestsForm,
    StudentProfileChangeForm,
    TeacherProfileChangeForm,
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
        kwargs["usernames"] = "!".join(
            [user.username for user in list(User.objects.all())]
        )
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


# @method_decorator([login_required, student_required], name="dispatch")
class StudentInterestsView(UpdateView):
    model = Student
    form_class = StudentInterestsForm
    template_name = "interests_form.html"

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, "Interests updated with success!")
        return super().form_valid(form)

    def get_success_url(self):
        user = self.get_object()
        return reverse("student_profile", kwargs={"pk": user.pk})


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherCreationForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "teacher"
        kwargs["usernames"] = "!".join(
            [user.username for user in list(User.objects.all())]
        )
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class StudentProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = "student_profile.html"

    def test_func(self):
        user = self.get_object()
        return user.is_student


class TeacherProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = "teacher_profile.html"

    def test_func(self):
        user = self.get_object()
        return user.is_teacher


class StudentProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = StudentProfileChangeForm

    template_name = "student_profile_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def get_success_url(self):
        user = self.get_object()
        return reverse("student_profile", kwargs={"pk": user.pk})


class TeacherProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = TeacherProfileChangeForm
    template_name = "teacher_profile_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def get_success_url(self):
        user = self.get_object()
        return reverse("teacher_profile", kwargs={"pk": user.pk})
