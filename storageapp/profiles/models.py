from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    adress = models.CharField(max_length=200, blank=True, null=True)
    contacts = models.CharField(max_length=200, blank=True, null=True)
