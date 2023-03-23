from rest_framework import serializers
from .action_seralizer import ActionSerializer
from ..models.hero import Hero

class HeroSerializer(serializers.ModelSerializer, ActionSerializer):
    description = serializers.CharField(allow_null=True, required=False)
    
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        not_fields = kwargs.pop('not_fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if not_fields is not None:
            for item in not_fields:
                self.fields.pop(item)
    
    class Meta:
        model = Hero
        fields = [
            'id',
            'name',
            'power',
            'description',
            'createdAt',
            'updatedAt',
            'deletedAt',
        ]