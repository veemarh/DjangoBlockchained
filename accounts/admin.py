from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User, Subject, Student, Teacher


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = [
        "email",
        "username",
        "birth_date",  # Нахуя тут дата рождения? Позже уберу
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("birth_date",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("birth_date",)}),)


class InterestsInline(admin.TabularInline):
    model = Subject


class StudentAdmin(admin.ModelAdmin):
    inlines = [InterestsInline]


admin.site.register(User, CustomUserAdmin)

admin.site.register(Student)

admin.site.register(Subject)

admin.site.register(Teacher)
