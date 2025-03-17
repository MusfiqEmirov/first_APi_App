from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http.response import Http404
from django.db import transaction
# from django.conf import settings
# from rest_framework.exceptions import NotFound

from first_app.models import Product, Category, Adress, Supplier
from first_app.serializers import (ProductSerializer,
                                  CategorySerializer,
                                  AddressSerializer,
                                  SupplierSerializer,
                                  ProductCreateSerializer,
                                  SupplierCreateSerializer
                                  )

# from notifications.notify import (
#     send_product_creation_email,
#     send_category_creation_email,
#     send_address_creation_email,
#     send_supplier_creation_email,
# )


class ProductsAPIView(APIView):
    # get methodu ile melumatlari getirmey  
    def get(self, request):
        products = Product.objects.all() # butun obyekctleri aliriq
        serializer = ProductSerializer(products,many=True) # birden daha cox abyekt olacagini qeyd edirik
        return Response(serializer.data)
    
    # post ile elave elemek
    def post(self,request):
        #json melumatlarini evvelce parse edirik
        serializer = ProductCreateSerializer(data=request.data) 
        if serializer.is_valid(): # validation gedir
            try:
                with transaction.atomic(): # ya hamisi isleyecek ve mail gedecek
                    serializer.save()
                    # ugurlu melyatda 201 status kodu qaytarir ve elave olundu
                    return Response(serializer.data, status=status.HTTP_201_CREATED) 
            except Exception as e: # ya hec biri iwlemeiyecek mailde getm,eyecek
                # eger mail gonderme alinmazsa
                transaction.set_rollback(True)
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         # yox eger ugursuzdusa yalniw sorgu olaraq geri qayatrir
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # secilen mehsulu qismen yenilemek.id urlde deyilde sonradan verilir ve ona gorede update olunur
    def patch(self, request):
        data = request.data
        id = data.get("id", None)
        product = Product.objects.filter(pk=id).first()
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        data = request.data
        id = data.get("id", None)
        if id:
            product = Product.objects.filter(id=id).first()
            product.delete()
            return Response({"message": "secdiyiniz mehsu; ugurla silindi!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "mehsul yoxdurr!!!"}, status=status.HTTP_400_BAD_REQUEST)

        
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
    
    @transaction.atomic
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # secilen categoiyani qismen yenilemek.id urlde deyilde sonradan verilir ve ona gorede update olunur
    def patch(self, request):
        data = request.data
        id = data.get("id", None)
        category = Category.objects.filter(pk=id).first()
        serializer = CategorySerializer(category,
                                         data=request.data,
                                         partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # categoryinain ozu ancaq id ile silinir
    def delete(self, request):
        data = request.data
        id = data.get("id", None)
        if id:
            category = Category.objects.filter(id=id).first()
            category.delete()
            return Response({"message": "secdiyiniz categoiya ugurla silindi!"}, 
                            status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "categoriya yoxdur yoxdurr!!!"},
                         status=status.HTTP_400_BAD_REQUEST)


# idye gor axtris
class CategoryRevealerAPIView(APIView):
    def get(self,request,id):
        category = get_object_or_404(Category ,id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

# category secdiyiiz butun productlari getirmek
class CategoryNameRevealerAPIView(APIView):
    
    def get(self, request, name):
        # mantto many oldugu ucun filterdir
        category = Category.objects.filter(name=name) 
        if not category.exists(): # eger secdiyimiz category yoxdusa qaytaracag cavab
            raise Http404("secilmis category uze mehsul tapilmadi!!!!")
        products = Product.objects.filter(categories__in=category) 
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    
    # secilmiw categoryde olan butun productlarin silinmesi
    def delete(self, request, name):
        category = Category.objects.filter(name=name)
        if not category.exists():
            raise Http404("secilmiw category uzre mehsul tapilmadi")
        products = Product.objects.filter(categories__in=category)
        products.delete()
        return Response({"message": "secdiyiniz categoriyay  uygun butun productlar silindi silindi!"},
                         status=status.HTTP_204_NO_CONTENT)


# Addres cagirilmasi ve elave olunmasi
class AddressAPIview(APIView):

    def get(self,request):
        address = Adress.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)
    
    @transaction.atomic
    def post(self,request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # secilen adreesi qismen yenilemek.id urlde deyilde sonradan verilir ve ona gorede update olunur
    def patch(self, request):
        data = request.data
        id = data.get("id", None)
        product = Adress.objects.filter(pk=id).first()
        serializer = AddressSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        data = request.data
        id = data.get("id", None)
        if id:
            address = Adress.objects.filter(id=id).first()
            address.delete()
            return Response({"message": "secdiyiniz adress ugurla silindi!"}, 
                            status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "adress yoxdurr!!!"}, 
                        status=status.HTTP_400_BAD_REQUEST)


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
    
    @transaction.atomic
    def post(self,request):
        # yenide yaratmagcun SerializerCreateSerilizerdennistifade olunur.cunki addresden Id gotur
        serializer = SupplierCreateSerializer(data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
     # secilen sirkeeti qismen yenilemek.id urlde deyilde sonradan verilir ve ona gorede update olunur
    def patch(self, request):
        data = request.data
        id = data.get("id", None)
        supplier = Supplier.objects.filter(pk=id).first()
        serializer = SupplierSerializer(supplier, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        data = request.data
        id = data.get("id", None)
        if id:
            supplier = Supplier.objects.filter(id=id).first()
            supplier.delete()
            return Response({"message": "secdiyiniz sirket ugurla silindi!"}, 
                            status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "sirket yoxdurr!!!"}, 
                        status=status.HTTP_400_BAD_REQUEST)

    
# secilmiw adress IDsine gore sirketi tapmag
class SupplierRevealerAPIView(APIView):

    def get(self, request, id):
        address = get_object_or_404(Adress, pk=id ) 
        active_supplier = Supplier.objects.get(address=address)  
        merchant_serializer = SupplierSerializer(active_supplier)
        return Response(merchant_serializer.data, status=status.HTTP_200_OK) 


# sirket adina gore axtaris
class SupplierCompanyNameRevealerAPIView(APIView):

    def get(self,request,company_name):
        company_name = get_object_or_404(Supplier, company_name=company_name)
        serializer = SupplierSerializer(company_name)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


    
        