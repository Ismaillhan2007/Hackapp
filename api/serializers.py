from rest_framework import serializers
from .models import CustomUser,Events

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','bio','avatar','city','is_superuser']
        read_only_fields = ['is_superuser']

class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only = True)

    class Meta:
        model = Events
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

