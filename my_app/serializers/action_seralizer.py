from rest_framework import serializers

class ActionSerializer(serializers.Serializer):
    createdAt = serializers.DateTimeField(source='created_at', required=False, allow_null=True)
    updatedAt = serializers.DateTimeField(source='updated_at', required=False, allow_null=True)
    deletedAt = serializers.DateTimeField(source='deleted_at', required=False, allow_null=True)