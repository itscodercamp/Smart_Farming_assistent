# Generated by Django 4.1.2 on 2023-02-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_alter_farming_product_list_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farming_product_list',
            name='rate',
            field=models.CharField(blank=True, max_length=220, null=1000),
        ),
    ]
