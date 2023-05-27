from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.models


class CustomManagerModel(BaseUserManager):
    def create_user(self, dni, email, password=None,
                    admin_pass=None, **extra_fields):
        if not dni and email:
            raise ValueError('The DNI field must provided')

        email = self.normalize_email(email)
        user = self.model(dni=dni, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, admin_pass=None,
                         **extra_fields):
        if not admin_pass:
            raise ValueError('You must provide an admin pass to be admin')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_superuser(email, password,
                                     admin_pass, **extra_fields)


class CustomUserModel(AbstractUser):
    STUDENT = 1
    TEACHER = 2
    ADMINISTRADOR = 3
    ROLE_CHOICES = ((STUDENT, 'student'),
                    (TEACHER, 'Teacher'),
                    (ADMINISTRADOR, 'Admin'))
    dni = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=30)
    has_rented = models.BooleanField(default=False)
    has_report = models.BooleanField(default=False)
    number_of_books_allowed = models.BooleanField(default=1)
    cupon = models.BooleanField(default=False)
    # only if the user provides the admin_pass will be admin
    admin_pass = models.CharField(default=None, max_length=10)
    role = models.CharField(max_length=10,
                            choices=ROLE_CHOICES, default='student')
    objects = CustomManagerModel()

    def save(self, *args, **kwargs):
        if self.role == 'student':
            self.number_of_books_allowed = 2
        elif self.role == 'teacher' or self.role == 'admin':
            self.number_of_books_allowed = 4
