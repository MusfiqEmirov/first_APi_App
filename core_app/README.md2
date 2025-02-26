# Django REST Framework API Documentation

This project provides a set of APIs for managing **Products**, **Categories**, **Addresses**, and **Suppliers** using Django REST Framework.

---

## Models

### 1. **Category**
- **Fields:**
  - `name` (CharField): The name of the category.

### 2. **Address**
- **Fields:**
  - `street` (CharField): The street name of the address.
  - `post_index` (CharField): The postal index of the address.
  - `city` (CharField): The city of the address.

### 3. **Supplier**
- **Fields:**
  - `company_name` (CharField): The name of the supplier company.
  - `address` (OneToOneField): A one-to-one relationship with the `Address` model.

### 4. **Product**
- **Fields:**
  - `name` (CharField): The name of the product.
  - `price` (FloatField): The price of the product.
  - `description` (CharField): A short description of the product.
  - `imageUrl` (CharField): The URL of the product image.
  - `categories` (ManyToManyField): A many-to-many relationship with the `Category` model.
  - `isActive` (BooleanField): Indicates whether the product is active.
  - `slug` (SlugField): A unique slug for the product.
  - `supplier` (ForeignKey): A foreign key relationship with the `Supplier` model.

---

## Serializers

### 1. **AddressSerializer**
- Used for CRUD operations on the `Address` model.
- **Fields:** All fields.

### 2. **SupplierSerializer**
- Used for CRUD operations on the `Supplier` model.
- **Fields:** All fields.

### 3. **SupplierCreateSerializer**
- Used for creating a new supplier.
- **Fields:** All fields, with `address` as a `PrimaryKeyRelatedField`.

### 4. **CategorySerializer**
- Used for CRUD operations on the `Category` model.
- **Fields:** All fields.

### 5. **ProductSerializer**
- Used for CRUD operations on the `Product` model.
- **Fields:** All fields.

### 6. **ProductCreateSerializer**
- Used for creating a new product.
- **Fields:** All fields, with `supplier` and `categories` as `PrimaryKeyRelatedField`.

---

## API Endpoints

### Products

- **GET** `/products/` - Retrieve all products.
- **POST** `/products/` - Create a new product.
- **PATCH** `/products/` - Partially update a product by ID.
- **DELETE** `/products/` - Delete a product by ID.

#### Product by ID
- **GET** `/products/<int:id>/` - Retrieve a product by ID.

#### Product by Slug
- **GET** `/products/<slug:slug>/` - Retrieve a product by slug.

### Categories

- **GET** `/categorys/` - Retrieve all categories.
- **POST** `/categorys/` - Create a new category.
- **PATCH** `/categorys/` - Partially update a category by ID.
- **DELETE** `/categorys/` - Delete a category by ID.

#### Category by ID
- **GET** `/categorys/<int:id>/` - Retrieve a category by ID.

#### Products by Category Name
- **GET** `/categorys/<str:name>/` - Retrieve all products under a specific category by name.
- **DELETE** `/categorys/<str:name>/` - Delete all products under a specific category by name.

### Addresses

- **GET** `/address/` - Retrieve all addresses.
- **POST** `/address/` - Create a new address.
- **PATCH** `/address/` - Partially update an address by ID.
- **DELETE** `/address/` - Delete an address by ID.

#### Address by ID
- **GET** `/address/<int:id>/` - Retrieve an address by ID.

#### Address by City
- **GET** `/address/<str:city>/` - Retrieve an address by city.

### Suppliers

- **GET** `/supplier/` - Retrieve all suppliers.
- **POST** `/supplier/` - Create a new supplier.
- **PATCH** `/supplier/` - Partially update a supplier by ID.
- **DELETE** `/supplier/` - Delete a supplier by ID.

#### Supplier by ID
- **GET** `/supplier/<int:id>/` - Retrieve a supplier by ID.

#### Supplier by Company Name
- **GET** `/supplier/<str:company_name>/` - Retrieve a supplier by company name.

---

## How to Use

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run migrations using `python manage.py migrate`.
4. Start the development server using `python manage.py runserver`.
5. Access the API endpoints as described above.

---

## Notes

- Ensure that the `address` is created before creating a `supplier`, as the `supplier` requires an `address` ID.
- For creating a `product`, ensure that the `supplier` and `categories` already exist, as they are required fields.

---
