from typing import Iterable
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Manager del modelo de usuario
class CustomUserManager(BaseUserManager):
    def generate_username(self, email):
        base_username = email.split('@')[0]
        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        return username

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        username = self.generate_username(email)
        if not email:
            raise ValueError(('El Email es obligatorio'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        username = self.generate_username(email)
        self.model(username=username, email=email, **extra_fields)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

# Modelo de usuario
class User(AbstractUser):
    """
    Modelo de usuario personalizado
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=800, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name',]
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email