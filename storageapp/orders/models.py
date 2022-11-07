from django.db import models
from profiles.models import Profile
from items.models import Item

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    newitem = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_created=True)
    is_active = models.BooleanField(default=True)
