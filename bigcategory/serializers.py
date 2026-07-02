from rest_framework import serializers
from .models import BigCategory

class BigCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = BigCategory
        fields = '__all__'