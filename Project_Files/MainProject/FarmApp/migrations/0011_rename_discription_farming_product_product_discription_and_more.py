# Generated by Django 4.1.4 on 2022-12-19 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FarmApp', '0010_rename_product_discription_farming_product_discription_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farming_product',
            old_name='Discription',
            new_name='product_discription',
        ),
        migrations.RenameField(
            model_name='farming_product',
            old_name='Images',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='farming_product',
            old_name='title',
            new_name='product_name',
        ),
    ]
