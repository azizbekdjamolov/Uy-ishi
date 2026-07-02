from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

# Create your views here.

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return[AllowAny()]
        
    #     return[IsAuthenticated()]