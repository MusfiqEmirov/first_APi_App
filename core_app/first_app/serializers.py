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


    def create(self, new_data):
        address_data = new_data.pop('address')  
        address = Adress.objects.create(**address_data) # yawasin gpt
        
        supplier = Supplier.objects.create(address=address, **new_data)
        return supplier


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all()) # yawasin gpt

    def create(self, new_product):
        categories_data = new_product.pop('categories', [])
        supplier_data = new_product.pop('supplier', None)
        
        # yeni mehsul yaratmag
        product = Product.objects.create(supplier=supplier_data, **new_product)

        # Categoriesi elaqelendirmelk
        product.categories.set(categories_data)  # ManyToMany elaqesi qurur
        return product
    
    class Meta:
        model = Product
        fields = "__all__"
