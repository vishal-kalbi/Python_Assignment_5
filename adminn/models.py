from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name


class ProdcutSubCategory(models.Model):
    price=models.CharField(max_length=150)
    product_pic=models.FileField(upload_to='product_pic',default="sad.png")
    product_model=models.CharField(max_length=150)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.price


            
    