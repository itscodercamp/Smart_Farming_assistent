# Generated by Django 4.1.4 on 2022-12-21 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarmApp', '0015_alter_farming_equpments_category'),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farming_product_list',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='FarmApp.category'),
        ),
    ]
