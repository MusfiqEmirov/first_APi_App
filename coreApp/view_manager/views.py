from rest_framework.views import APIView,status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from firstApp.models import Product
from firstApp.serializers import ProductSerializer


class ProductsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all() # butun obyekctleri aliriq
        serializer = ProductSerializer(products,many=True) # birden daha cox abyekt olacagini qeyd edirik
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data) #json melumatlarini evvelce parse edirik

        if serializer.is_valid(): # validation gedir
            serializer.save() # ve yaddawa yazir
            return Response(serializer.data, status=status.HTTP_201_CREATED) # ugurlu melyatda 201 status kodu qaytarir ve elave olundu
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # yox eger ugursuzdusa yalniw sorgu olaraq geri qayatrir

