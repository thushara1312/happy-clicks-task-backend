from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'date_added', 'date_updated']

    def create(self, validated_data):
        user = self.context['user']
        return Task.objects.create(user=user, **validated_data)
    
    def update(self, instance, validated_data):
        # Ensure user can't be changed
        validated_data.pop('user', None)
        return super().update(instance, validated_data)