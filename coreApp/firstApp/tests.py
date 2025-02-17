from rest_framework.test import APITestCase
from rest_framework import status
from firstApp.models import Product
from django.urls import reverse


# mehsullarin duzgun alinib ve getirlmeyi baresinde test
class ProductsAPIViewTest(APITestCase):
    def setUp(self):
        # testden evvel bezi mehsullar elave edirkk
        Product.objects.create(name="product name1",price=100)
        Product.objects.create(name="product name2",price=200)

    def test_get_products(self):
        # get methodu ile mehsullarin duzgun alindigini yoxlayiriq
         url = reverse('products')  # verdiyimiz endpoit nameni yaziriq
         response = self.client.get(url)

         #status kodunu yoxlayiriq 200 olamldir
         self.assertEqual(response.status_code,status.HTTP_200_OK)

         # verilenlerin duzgun oldugunu yoxlamag
         self.assertEqual(len(response.data),2)  # yeni 2 mehsul olmalidir
         self.assertEqual(response.data[0]["name"], "product name1") # bu birinci mehsulun adi
         self.assertEqual(response.data[1]["name"], "product name2") # bu ikinci mehsulun adi

        