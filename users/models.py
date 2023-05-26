from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.models


class CustomUserManager(BaseUserManager):
    def create_user(self, dni, password, **extra_fields):
        if not dni:
            raise ValueError(("The DNI must be set"))

        user = self.model(dni=dni, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        pass


class BaseUser(AbstractBaseUser):
    dni = models.CharField(primary_key=True, max_length=8, editable=False)
    phone = models.CharField(max_length=10)
    user_name = models.CharField(max_length=20)
    secondName = models.CharField(max_length=20, default=None)
    lastName = models.CharField(max_length=15)
    email = models.EmailField()
    objects = CustomUserManager()

    def __str__(self):
        return self.user_name

    class Meta:
        default_related_name = 'base_users'


class TeacherUser(BaseUser):
    university_department = models.CharField(max_length=20)
    has_rented = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'teachers_users'


class StudentUser(BaseUser):
    carrer = models.CharField(max_length=20)
    has_rented = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'students_users'


class AdminLibrary(BaseUser):
    last_report = models.DateField()

    class Meta:
        default_related_name = 'admin_library_users'
