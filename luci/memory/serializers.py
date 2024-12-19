from rest_framework import serializers
from .models import ProjectMemory

class ProjectMemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMemory
        fields = '__all__'
