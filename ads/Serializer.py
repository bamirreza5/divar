from rest_framework import serializers
from .models import Ad

# class AdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ad
#         exclude = ['user']

#     def create(self, validated_data):
#         validated_data['user'] = self.context['request'].user
#         return super().create(validated_data)
class AdSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Ad
        fields = '__all__'
