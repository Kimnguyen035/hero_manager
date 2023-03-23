from rest_framework import serializers
from ..models.hero import Hero
from configs.variable_response import *

class IdHeroValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    def validate_id(self, value):
        querryset = Hero.objects.filter(id=value)
        if not querryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        return value
    