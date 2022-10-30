from django.db import models




class Company(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=300)

class EquipTag(models.Model):
    name = models.CharField(max_length=30)
    companies = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

class Item(models.Model):
    name = models.CharField(max_length=30)
    amount = models.PositiveIntegerField(default=0)
    position = models.CharField(max_length=10, blank=True, null=True)
    tags = models.ManyToManyField(EquipTag)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)