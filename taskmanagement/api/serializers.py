from rest_framework import serializers

from .models import Task, Status


# Task serializer with required fields
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'story_point']


# Status serializer with required field
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['status']

