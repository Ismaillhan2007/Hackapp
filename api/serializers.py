from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','bio','avatar','city','is_superuser']
        # read_only_fields = ['is_superuser']







    