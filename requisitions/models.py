from django.db import models

# Create your models here.
# requisitions/models.py
from django.contrib.auth.models import User

class Requisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    approved = models.BooleanField(default=False)

    def calculate_deposit(self):
        if self.amount:
            return self.amount * 0.6
        return 0
