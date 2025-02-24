from rest_framework import serializers
from .models import *

#adress modeli uzerinde CRUD EMELIYATLARI
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields = "__all__"

#SUPPLIER modeli uzerinde CRUD EMELIYATLARI
class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"

# ONETOONE OLDUGU UCUN EVVELCE ADRESS ELAVE OLUNMALI SOSRA ONUN IDSI YAZILMALDIIR
class SupplierCreateSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(queryset=Adress.objects.all())

    class Meta:
        model = Supplier
        fields = "__all__"



# CATEGORYS UZERINDE CRUD EMELIYATLARI
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


#  PRODUCTS UZERINDE CRUD EMELIYATLARI
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


# MANY TOI MAY OLDUGU UCUN RAHAT WEKILDE ISTENILEN CATEGORYDEN ALA BILER IDISINI
class ProductCreateSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = "__all__"      
