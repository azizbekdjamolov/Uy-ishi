from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
    def validate(self, attrs):
        big_category = attrs.get("big_category")
        category = attrs.get("category")
    
        if category.big_category != big_category:
            raise serializers.ValidationError({
                "error": "Tanlangan category ushbu big category'ga tegishli emas."
            })
    
        return attrs