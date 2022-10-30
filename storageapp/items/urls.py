from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from items.views import *

app_name = 'items'

urlpatterns = [
     path('index/', ItemAPIListView.as_view()),
     path('index/<int:pk>/', ItemAPIUpdateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)