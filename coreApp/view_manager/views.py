from rest_framework.views import APIView,status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from firstApp.models import Product
from firstApp.serializers import ProductSerializer
from django.shortcuts import get_object_or_404


class ProductsAPIView(APIView):
    # get methodu ile melumatlari getirmey  
    def get(self, request):
        products = Product.objects.all() # butun obyekctleri aliriq
        serializer = ProductSerializer(products,many=True) # birden daha cox abyekt olacagini qeyd edirik
        return Response(serializer.data)
    
    # post ile elave elemek
    def post(self,request):
        serializer = ProductSerializer(data=request.data) #json melumatlarini evvelce parse edirik

        if serializer.is_valid(): # validation gedir
            serializer.save() # ve yaddawa yazir
            return Response(serializer.data, status=status.HTTP_201_CREATED) # ugurlu melyatda 201 status kodu qaytarir ve elave olundu
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # yox eger ugursuzdusa yalniw sorgu olaraq geri qayatrir


# idye gor axtris
class ProductRevealerAPIView(APIView):
    def get(self,request,id):
        product = get_object_or_404(Product ,id=id)

        serializer = ProductSerializer(product)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

# slug ile axtariw ucun
class ProductSlugRevealerAPIView(APIView):
    def get(self,request,slug):
        product = get_object_or_404(Product ,slug=slug)

        serializer = ProductSerializer(product)
        
        return Response(serializer.data,status=status.HTTP_200_OK)