# Generated by Django 5.1.4 on 2024-12-23 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_playground_joined_data_playground_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playground',
            old_name='joined_data',
            new_name='joined_date',
        ),
    ]
