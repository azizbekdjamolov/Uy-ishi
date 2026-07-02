from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelField):
    class Meta:
        model = Post
        exclude = ['created_at']