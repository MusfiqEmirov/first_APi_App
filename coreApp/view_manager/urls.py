from django.urls import path
from .views import *

urlpatterns = [
    path("products", ProductsAPIView.as_view(), name="products")
]
