# Generated by Django 4.1.4 on 2022-12-21 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FarmApp', '0016_delete_farming_equpments'),
        ('Products', '0003_alter_farming_product_list_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farming_Equpments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equpement_name', models.CharField(max_length=255)),
                ('equpement_discription', models.TextField()),
                ('equpement_image', models.ImageField(blank=True, help_text='Ex : use 1500x500 px its suitabler', max_length=555, null=True, upload_to='media/equpement_img')),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='FarmApp.category')),
            ],
        ),
    ]
