from django.db import models




class Company(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=300)


class Item(models.Model):
    name = models.CharField(max_length=30)
    amount = models.PositiveIntegerField(default=0)
    position = models.CharField(max_length=10, blank=True, null=True)
    tags = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)