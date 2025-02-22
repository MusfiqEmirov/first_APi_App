from django.urls import path
from .views import *

app_name = "view_manager"
urlpatterns = [
    # product viewi
    path("products/", ProductsAPIView.as_view(), name="products"),
    path("products/<int:id>/", ProductRevealerAPIView.as_view(), name="products_id_details"),
    path("products/<slug:slug>/", ProductSlugRevealerAPIView.as_view(), name="products_slug_details"),

    # category viewi
    path("categorys/", CategoryAPIView.as_view(), name="categorys"),
]
