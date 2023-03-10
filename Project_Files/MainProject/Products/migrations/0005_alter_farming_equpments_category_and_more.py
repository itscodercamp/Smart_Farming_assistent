# Generated by Django 4.1.4 on 2022-12-21 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
        ('Products', '0004_farming_equpments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farming_equpments',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Category.category'),
        ),
        migrations.AlterField(
            model_name='farming_product_list',
            name='category',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Category.category'),
        ),
    ]
