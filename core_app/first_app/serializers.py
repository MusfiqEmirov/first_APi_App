from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Supplier
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
