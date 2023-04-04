from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=10, blank=False)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username}'