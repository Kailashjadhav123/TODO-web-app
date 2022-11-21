from todo_list.models import List
from .serializers import ListSerializer
from rest_framework import viewsets


class ListSerializerview(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
