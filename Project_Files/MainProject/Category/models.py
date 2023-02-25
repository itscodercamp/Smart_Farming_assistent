from django.db import models


#  catagory for All fields
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
