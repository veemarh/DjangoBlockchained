from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import StudentUser, TeacherUser


class StudentUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = StudentUser
        fields = (
            "first_name",
            "second_name",
            "third_name",
            "phone_number" "email",
            "age",
        )


class StudentUserChangeForm(UserChangeForm):
    class Meta:
        model = StudentUser
        fields = (
            # "first_name",
            # "second_name", Допустим студент не может поменять свое имя?
            # "third_name",
            "phone_number",
            "school_name",
            "birth_date" "email",
            "age",
        )

