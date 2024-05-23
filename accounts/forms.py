from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from .models import Student, Teacher, Subject, User


class StudentCreationForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "second_name",
            "email",
            "phone_number",
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get("interests"))
        return user


class StudentInterestsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("interests",)
        widgets = {"interests": forms.CheckboxSelectMultiple}


class TeacherInterestsForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("interests",)
        widgets = {"interests": forms.CheckboxSelectMultiple}


class TeacherCreationForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "second_name",
            "email",
            "phone_number",
        )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )


class StudentProfileChangeForm(forms.ModelForm):
    school_name = forms.CharField()

    class Meta:
        fields = (
            "username",
            "first_name",
            "second_name",
            "third_name",
            "birth_date",
            "phone_number",
            "email",
        )
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.student.school_name = self.cleaned_data.get("school_name")
        user.save()
        user.student.save()
        return user


class TeacherProfileChangeForm(forms.ModelForm):
    description = forms.CharField()
    diploma = forms.CharField()
    experience = forms.CharField()

    class Meta:
        fields = (
            "username",
            "first_name",
            "second_name",
            "third_name",
            "birth_date",
            "phone_number",
            "email",
        )
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.teacher.description = self.cleaned_data.get("description")
        user.teacher.diploma = self.cleaned_data.get("diploma")
        user.teacher.experience = self.cleaned_data.get("experience")
        user.save()
        user.teacher.save()
        return user
