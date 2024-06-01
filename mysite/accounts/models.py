from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    OWNER = 'Owner'
    CUSTOMER = 'Customer'
    BLOCKED = 'Blocked'
    ROLE_CHOICES = [
        (OWNER, 'Owner'),
        (CUSTOMER, 'Customer'),
        (BLOCKED,  'Blocked'),
    ]

    name = models.CharField(max_length=100, choices=ROLE_CHOICES, default=CUSTOMER)

    def __str__(self):
        return self.name 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.user.username}"
