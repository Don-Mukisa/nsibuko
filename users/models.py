from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    user_type_choices = [
        ('supervisor', 'Supervisor'),
        ('officer', 'Officer'),
        ('administrator', 'Administrator'),
    ]
    user_type = models.CharField(max_length=15, choices=user_type_choices)

    def __str__(self):
        return self.user.username
