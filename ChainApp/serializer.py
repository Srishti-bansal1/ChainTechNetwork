import datetime
from .models import ChainModel ,DataTable
from rest_framework import serializers

class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChainModel
        fields = ['name','email']
        
class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTable
        fields = ['name','email']
        
        
class DynamicSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    quotes = serializers.CharField()
    weather = serializers.JSONField()
    class Meta:
        fields = ['timestamp', 'quotes','weather']
    
