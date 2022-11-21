from rest_framework import serializers
from todo_list.models import List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'item', 'completed']
