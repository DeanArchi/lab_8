from django.shortcuts import render

from .models import Student, Subject, Exam


def index(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    exams = Exam.objects.all()

    return render(request, 'index.html', {
        'students': students,
        'subjects': subjects,
        'exams': exams,
    })
