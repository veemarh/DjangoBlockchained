from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = [
        "email",
        "username",
        "birth_date",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("birth_date",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("birth_date",)}),)
