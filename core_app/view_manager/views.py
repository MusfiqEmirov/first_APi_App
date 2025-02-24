from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from first_app.models import Product, Category, Adress, Supplier
from first_app.serializers import ProductSerializer, CategorySerializer, AddressSerializer, SupplierSerializer, ProductCreateSerializer, SupplierCreateSerializer
from django.shortcuts import get_object_or_404
from django.http.response import Http404


class ProductsAPIView(APIView):
    # get methodu ile melumatlari getirmey  
    def get(self, request):
        products = Product.objects.all() # butun obyekctleri aliriq
        serializer = ProductSerializer(products,many=True) # birden daha cox abyekt olacagini qeyd edirik
        return Response(serializer.data)
    
    # post ile elave elemek
    def post(self,request):
        serializer = ProductCreateSerializer(data=request.data) #json melumatlarini evvelce parse edirik

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
    

class CategoryAPIView(APIView):
    #get ile categpryleri getirmek
    def get(self,request):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# idye gor axtris
class CategoryRevealerAPIView(APIView):
    def get(self,request,id):
        category = get_object_or_404(Category ,id=id)
        serializer = CategorySerializer(category)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
# name ile axtariw ucun
class CategoryNameRevealerAPIView(APIView):
    
    def get(self, request, name):
        
        category = Category.objects.filter(name=name)  

        if category.count() < 1:
            raise Http404("secilmis category uze mehsul tapilmadi!!!!")
        
        products = Product.objects.filter(categories__in=category) 
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)


# Addres cagirilmasi ve elave olunmasi
class AddressAPIview(APIView):

    def get(self,request):
        address = Adress.objects.all()
        serializer = AddressSerializer(address, many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer = AddressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# idye gor axtris
class AddressRevealerAPIView(APIView):
    def get(self, request, id):
        address = get_object_or_404(Adress ,id=id)
        serializer = AddressSerializer(address)

        return Response(serializer.data,status=status.HTTP_200_OK)   

# city  gor axtris ile axtariw ucun
class AddressCityRevealerAPIView(APIView):
    def get(self, request, city):
        address = get_object_or_404(Adress, city=city)
        serializer = AddressSerializer(address)
        
        return Response(serializer.data, status=status.HTTP_200_OK)   


# Supplier cagirilmasi ve elave olunmasi
class SupplierAPIview(APIView):

    def get(self,request):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer = SupplierCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SupplierRevealerAPIView(APIView):
    def get(self, request, id):
        address = get_object_or_404(Adress, pk=id ) 
        sup = Supplier.objects.get(address=address)  
        sup_serializer = SupplierSerializer(sup)
        return Response(sup_serializer.data, status=status.HTTP_200_OK) 


class SupplierCompanyNameRevealerAPIView(APIView):

    def get(self,request,company_name):
        company_name = get_object_or_404(Supplier, company_name=company_name)
        serializer = SupplierSerializer(company_name)
        
        return Response(serializer.data,status=status.HTTP_200_OK)



    
        