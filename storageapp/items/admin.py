from django.contrib import admin

from items.models import Company, EquipTag, Item

admin.site.register(Company)
admin.site.register(EquipTag)
admin.site.register(Item)

