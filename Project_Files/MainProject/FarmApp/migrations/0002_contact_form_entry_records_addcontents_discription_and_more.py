# Generated by Django 4.1.4 on 2022-12-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Form_Entry_Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flrstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='addcontents',
            name='Discription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='addcontents',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
