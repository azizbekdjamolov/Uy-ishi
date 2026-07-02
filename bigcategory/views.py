from rest_framework import generics
from .models import BigCategory
from .serializers import BigCategorySerializers


class BigCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BigCategory.objects.all()
    serializer_class = BigCategorySerializers


class BigCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BigCategory.objects.all()
    serializer_class = BigCategorySerializers