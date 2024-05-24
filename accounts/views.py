from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    UpdateView,
    TemplateView,
    DetailView,
)

from .decorators import student_required, teacher_required
from .forms import (
    StudentCreationForm,
    TeacherCreationForm,
    StudentInterestsForm,
    TeacherInterestsForm,
    StudentProfileChangeForm,
    TeacherProfileChangeForm,
)
from .models import User, Student, Teacher


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


@method_decorator([login_required, student_required], name="dispatch")
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


@method_decorator([login_required, teacher_required], name="dispatch")
class TeacherInterestsView(UpdateView):
    model = Teacher
    form_class = TeacherInterestsForm
    template_name = "interests_form.html"

    def get_object(self):
        return self.request.user.teacher

    def form_valid(self, form):
        messages.success(self.request, "Interests updated with success!")
        return super().form_valid(form)

    def get_success_url(self):
        user = self.get_object()
        return reverse(
            "teacher_profile", kwargs={"pk": user.pk}
        )  # Как это работает вообще?


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


# class StudentProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
class StudentProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "student_profile.html"

    # def test_func(self):
    #     user = self.get_object()
    #     return user.is_student

    def add_to_student_list(self, request, *args, **kwargs):
        teacher = request.user.teacher
        user = self.get_object()
        user.student.teacher_list.append(teacher)
        user.student.save()
        return reverse("student_profile", kwargs={"pk": user.pk})

    def get_context_data(self, **kwargs):
        kwargs["add_to_student_list"] = self.add_to_student_list
        return super().get_context_data(**kwargs)


# class TeacherProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
class TeacherProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "teacher_profile.html"

    # def test_func(self):
    #     user = self.get_object()
    #     return user.is_teacher


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


def add_to_teacher_list(request, pk, *args, **kwargs):
    student = request.user.student
    teacher = get_object_or_404(Teacher, pk=pk)
    # print(teacher.user.username)
    student.teacher_list.add(teacher)
    student.save()
    # print(student.teacher_list.all())
    return redirect("teacher_profile", pk)


def remove_from_teacher_list(request, pk, *args, **kwargs):
    student = request.user.student
    teacher = get_object_or_404(Teacher, pk=pk)
    student.teacher_list.remove(teacher)
    student.save()
    return redirect("teacher_profile", pk)
