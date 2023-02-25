# Generated by Django 4.1.4 on 2022-12-21 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarmApp', '0015_alter_farming_equpments_category'),
        ('Products', '0002_farming_product_list_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farming_product_list',
            name='category',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FarmApp.category'),
        ),
    ]
