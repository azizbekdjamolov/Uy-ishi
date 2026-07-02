from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"]
        )

        if not user:
            raise serializers.ValidationError("Username yoki password xato.")

        attrs["user"] = user
        return attrs
    
class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','password']

class ProfileUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name']
