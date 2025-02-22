from rest_framework import serializers
from .models import Ad
from ads.models import Category, City

# class AdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ad
#         exclude = ['user']

#     def create(self, validated_data):
#         validated_data['user'] = self.context['request'].user
#         return super().create(validated_data)from rest_framework import serializers
from .models import Ad, Category, City

class AdSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Ad
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'city']

class CitySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = City
        fields = '__all__'
