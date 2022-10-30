from items.models import Item,EquipTag,Company
from rest_framework import serializers



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'