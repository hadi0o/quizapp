from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission


SEX_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

class Profile(models.Model):
    name = models.CharField(max_length=255)
    tel = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.PositiveIntegerField()
    field_of_study = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    sleep_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name
