# Generated by Django 4.1.4 on 2022-12-14 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FarmApp', '0002_contact_form_entry_records_addcontents_discription_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_form_entry_records',
            old_name='flrstname',
            new_name='firstname',
        ),
    ]
