from django.db import models
from django.contrib.auth.models import User


class Grade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    day_choices = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=day_choices)
    period = models.PositiveIntegerField()
    course_name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    teaching_plan = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.day} - Period {self.period}: {self.course_name}'
