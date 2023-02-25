from django.db import models

# Create your models here.
class Types_Of_Farming(models.Model):

    title = models.CharField(max_length=255, null=True,help_text='Ex : Add Title name at least 2 words remember this word not a single letter')
    slug = models.SlugField(null=True ,help_text='Ex : add Slugs like this in this section you can make it with your titlwe name insted of space use (-) like this (Cotton-Farming)')
    Discription = models.TextField(null=True)

    Images = models.ImageField(upload_to='media', max_length=555,null=True, blank=True ,help_text='Ex : use 1500x500 px its suitabler')
    def __str__(self):
        return self.title


class Contact_Form_Entry_Records(models.Model):
    
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.firstname


class Farming_Product(models.Model):

    product_name = models.CharField(max_length=255)
    product_discription = models.TextField()
    product_image = models.ImageField(upload_to='media/product_img', max_length=555,null=True, blank=True ,help_text='Ex : use 1500x500 px its suitabler')

    def __str__(self):
        return self.product_name






class Flower_farming(models.Model):

    topicName = models.CharField(max_length=255)
    topic_discription = models.TextField()
    cover_image = models.ImageField(upload_to='media/topic_img', max_length=555,null=True, blank=True ,help_text='Ex : use 1500x500 px its suitabler')

    def __str__(self):
        return self.topicName


