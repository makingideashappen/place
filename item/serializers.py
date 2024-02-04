# myapp/serializers.py
from rest_framework import serializers
from .models import Item,Category

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'category', 'name', 'description', 'price', 'image', 'is_sold', 'created_by', 'created_at']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']