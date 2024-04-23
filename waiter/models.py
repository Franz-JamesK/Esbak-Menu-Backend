from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import BaseUserManager

class Waiter(AbstractUser):
    # Add custom fields for Waiter
    employee_number = models.CharField(max_length=20, unique=True, default="DEFAULT_EMPLOYEE_NUMBER", validators=[MinLengthValidator(5)])
    phone_number = models.CharField(max_length=15, default="DEFAULT_PHONE_NUMBER")


    # Add related_name to resolve clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='waiter_groups',
        blank=True,
        help_text='The groups this waiter belongs to. A waiter will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='waiter_user_permissions',
        blank=True,
        help_text='Specific permissions for this waiter.'
    )

    def __str__(self):
        return self.username
