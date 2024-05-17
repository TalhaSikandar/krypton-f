from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(username, password, **extra_fields)
#
# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length=150, unique=True)
#     address = models.CharField(max_length=255)
#     company_code = models.CharField(max_length=10, unique=True)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['address', 'company_code']
#
#     def __str__(self):
#         return self.username
#

from django.contrib.auth.models import AbstractUser
from companies.models import Company

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    company_code = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, help_text="Your Company", related_name="users")
    USERNAME_FIELD = 'email'

    ADMIN = 1
    MANAGER = 2
    class Types(models.TextChoices):
            ADMIN = "ADMIN", "Admin"
            MANAGER = "MANAGER", "Manager"
    role = models.CharField(default=Types.MANAGER, max_length=10, choices=Types.choices, blank=False, null=False, help_text="Your role in the Company")
    REQUIRED_FIELDS = ['user_name', 'company_code', 'role']
