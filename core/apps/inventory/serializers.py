from rest_framework import serializers
from apps.inventory.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name','description','price','quantity','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at']

    
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        
        return value
    
    def validate_quantity(self,value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value