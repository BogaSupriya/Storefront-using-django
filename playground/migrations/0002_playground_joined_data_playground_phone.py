# Generated by Django 5.1.4 on 2024-12-23 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playground',
            name='joined_data',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='playground',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
