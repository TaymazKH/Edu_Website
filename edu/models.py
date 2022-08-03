from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.contrib.auth.models import User


class Course(models.Model):
    department = models.CharField(max_length=100, validators=[MinLengthValidator(limit_value=1, message="1")])
    name = models.CharField(max_length=100, validators=[MinLengthValidator(limit_value=1, message="2")])
    course_number = models.IntegerField(default=1, validators=[MinValueValidator(limit_value=1, message="3")])
    group_number = models.IntegerField(default=1, validators=[MinValueValidator(limit_value=1, message="4")])
    teacher = models.CharField(max_length=100, validators=[MinLengthValidator(limit_value=1, message="5")])
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.CharField(max_length=2, default=0, choices=(
        ('0', 'saturday'),
        ('1', 'sunday'),
        ('2', 'monday'),
        ('3', 'tuesday'),
        ('4', 'wednesday')
    ))
    second_day = models.CharField(max_length=2, default=0, choices=(
        ('0', 'saturday'),
        ('1', 'sunday'),
        ('2', 'monday'),
        ('3', 'tuesday'),
        ('4', 'wednesday'),
        ('7', '-')
    ))

    def __str__(self):
        return f"{self.name}({self.course_number}-{self.group_number})"


class Account(models.Model):
    bio = models.TextField(max_length=250, default="", blank=True)
    gender = models.CharField(max_length=10, default='undefined', choices=(('undefined', 'undefined'), ('male', 'male'), ('female', 'female')))
    profile_picture = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
