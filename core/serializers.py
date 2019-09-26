from rest_framework import serializers
from core.models import User

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_image',)
