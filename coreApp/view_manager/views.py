from rest_framework.views import APIView,status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from firstApp.models import Product
from firstApp.serializers import ProductSerializer


class ProductsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    

