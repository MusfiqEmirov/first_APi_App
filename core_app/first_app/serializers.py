from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Adress
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierCreateSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(queryset=Adress.objects.all())

    class Meta:
        model = Supplier
        fields = "__all__"




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class ProductCreateSerializer(serializers.ModelSerializer):
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = "__all__"      
