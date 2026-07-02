from rest_framework import status
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer,ProfileUpdateSerializers,MeSerializer
from rest_framework.generics import RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )
    
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Meview(RetrieveAPIView):
    serializer_class = MeSerializer
    permission_classes= [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class ProfileUpdateview(RetrieveUpdateAPIView):
    serializer_class = ProfileUpdateSerializers
    permission_classes= [IsAuthenticated]

    def get_object(self):
        return self.request.user