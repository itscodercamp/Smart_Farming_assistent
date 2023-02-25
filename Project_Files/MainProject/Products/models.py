from django.db import models
# from FarmApp.models import Category
from Category.models import Category

# Create your models here.
class Farming_Product_List(models.Model):
    images = models.ImageField(upload_to='media/ProductsApp', max_length=555,null=True, blank=True ,help_text='Ex : use 1500x500 px its suitabler')
    name = models.CharField(max_length=220)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=True, null=True)
    discription = models.TextField()
    rate = models.CharField(max_length=220 ,null=True, blank=True)

    def __str__(self):
        return self.name

class Farming_Equpments(models.Model):

    equpement_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=True)
    equpement_discription = models.TextField()
    equpement_image = models.ImageField(upload_to='media/equpement_img', max_length=555,null=True, blank=True ,help_text='Ex : use 1500x500 px its suitabler')

    def __str__(self):
        return self.equpement_name