from rest_framework.test import APITestCase
from rest_framework import status
from firstApp.models import Product
from django.urls import reverse


# mehsullarin duzgun alinib ve getirlmeyi baresinde test
class ProductsAPIViewTest(APITestCase):
    # get methodunun test edilmesi
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

    # post methodunun test edilmesi ve yeni mehsul elave edilmesi
    def test_post_product(self):
        url = reverse('products')
        data = {
            "name": "balli tort",
            "price": 5.9,
            "description":"en dadli tort",
            "imageUrl":"545.jpg",
            "isActive": True,
            "slug": "en-dadli-tort"
        }
        #POST sorgusu gonderirlr
        response = self.client.post(url,data,format="json")

        #status kodunun yoxlanilmasi
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # yeni mehsulun elave dildiyini yoxlamag
        self.assertEqual(response.data["name"], "balli tort")
        self.assertEqual(response.data["price"], 5.9)

        # yeni mehsulun data bazaya duwmesi yoxlanilir
        self.assertEqual(Product.objects.count(), 3) # burda artiq 3 mehsul olamlidir

    def test_post_invalid_product(self):
        #POST methodu ile qiymetsis gonderilse
        url = reverse("products")
        data = {
            "name": "no validation"
        }

        # post sorgusu  gonderilir
        response = self.client.post(url,data,format="json")

        # status kodu yoxlanilir
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # error mesaji yoxlanilir
        self.assertIn("price", response.data) # teleb olunan sahe


# idye gore melumat elde elemek ucun test
class ProductRevealerAPIViewTest(APITestCase):
    def setUp(self):
        # yene testden evvel bezi mehsullaar elav edirik
        self.product1 = Product.objects.create(name="product1",price=10)
        self.product2 = Product.objects.create(name="product2",price=20)

    def test_get_product_by_id(self):
        # idye gore dogru melumat almag
        url = reverse("view_manager:products_id_details",args=[self.product1.id])
        
        #get soprgusu gonderilir
        response = self.client.get(url)

        # status kodunun 200 olmagi yoxlanilir
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        # mehsulun duzgun qaytarilmagi yoxlanilir
        self.assertEqual(response.data["name"],"product1")
        self.assertEqual(response.data["proce"],10)

    def test_get_product_not_found(self):
        # eger id olmsa bize verilen cavab
        url = reverse("view_manager:products_id_details", args=[100])  # Bu id movcu deyil
        
        response = self.client.get(url)

        # status kodunun 404 olacagi yoxlanilir
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)




