# manager/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user_with_token(self, employee_number, email, password):
        # Create a user with the provided employee_number, email, and password
        user = self.model(
            employee_number=employee_number,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Manager(AbstractUser):
    # Add custom fields for Manager
    # For example:
    phone_number = models.CharField(max_length=15)
    employee_number = models.CharField(max_length=20, unique=True, default='00000000')
    objects = UserManager()

class Waiter(models.Model):
    employee_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(default='example@example.com')  # Default email value
    password = models.CharField(max_length=128)

    from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Drinks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    
    # Add related_name to resolve clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='manager_groups',
        blank=True,
        help_text='The groups this manager belongs to. A manager will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='manager_user_permissions',
        blank=True,
        help_text='Specific permissions for this manager.'
    )

    def __str__(self):
        return self.username
