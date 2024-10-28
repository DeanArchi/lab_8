from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    course = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], blank=True, null=True)
    faculty = models.CharField(max_length=50, choices=[('Agrarian management', 'Agrarian management'),
                                                       ('Economics', 'Economics'),
                                                       ('IT', 'IT')], blank=True, null=True)
    group_name = models.CharField(max_length=50, blank=True, null=True)
    is_leader = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    hours_per_semester = models.IntegerField()
    semesters_count = models.IntegerField()

    def __str__(self):
        return self.subject_name


class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5')])

    def __str__(self):
        return f"Exam for {self.student} in {self.subject} - Grade: {self.grade}"
