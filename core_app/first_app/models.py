from django.db import models
# from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
    
class Adress(models.Model):
     street = models.CharField(max_length=500) 
     post_index = models.CharField(max_length=50)        
     city = models.CharField(max_length=50) 

     def __str__(self):
          return f"{self.street} {self.post_index} {self.city}"
     

class Supplier(models.Model):
        company_name = models.CharField(max_length=100) 
        adress = models.OneToOneField(Adress,null=True,on_delete=models.CASCADE) 

        def __str__(self):
          return f"{self.company_name} {self.adress}" 


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=60)
    categories = models.ManyToManyField(Category)
    # category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="products")
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(default="", blank=True, null=False,db_index=True,unique=True)
    supplier = models.ForeignKey(Supplier,null=True,on_delete=models.CASCADE)

    # def save(self, *args,**kargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args,**kargs)  uje burda buna hetiyac olmur admin panelde ozu avtomatik verilir

    def __str__(self):
        return self.name
    

