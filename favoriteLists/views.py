from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.decorators import student_required, teacher_required


@login_required
@student_required
def getFavoriteTeachersList(request):

    student = request.user.student
    teachers = student.favorite_teachers.all()

    return render(request, "favorite_teachers.html", {"teachers": teachers})


@login_required
@teacher_required
def getFavoriteStudentsList(request):
    teacher = request.user.teacher
    students = [user.student for user in teacher.favorite_students.all()]

    return render(request, "favorite_students.html", {"students": students})
