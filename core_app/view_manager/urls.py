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
    path("categorys/<int:id>/", CategoryRevealerAPIView.as_view(), name="categorys_id_details"),

    # categpriyasini seciyimiz butun productlar
    path("categorys/<str:name>/", CategoryNameRevealerAPIView.as_view(), name="categorys_name_details"),

    # address viewi
    path("address/", AddressAPIview.as_view(), name="address"),
    path("address/<int:id>/", AddressRevealerAPIView.as_view(), name="address_id_details"),
    path("address/<str:city>/", AddressCityRevealerAPIView.as_view(), name="address_city_details"),

    # supplier viewi
    path("supplier/", SupplierAPIview.as_view(), name="supplier"),
    
    # adresi secmini elediyimiz tek supplier ucun
    path("supplier/<int:id>/", SupplierRevealerAPIView.as_view(), name="supplier_id_details"),
    path("supplier/<str:company_name>/", SupplierCompanyNameRevealerAPIView.as_view(), name="supplier_company_name_details"),
]