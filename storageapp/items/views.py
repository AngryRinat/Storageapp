from rest_framework.viewsets import ViewSet
from items.models import *
from items.serializers import *

class ItemAPIViewSet(ViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

