from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("customer", "Customer"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="customer")
    phone = models.CharField(max_length=15, blank=True, null=True)  # Đảm bảo có trường này

    def __str__(self):
        return f"{self.username} - {self.role}"