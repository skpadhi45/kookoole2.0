# Generated by Django 4.1.3 on 2023-08-06 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0015_alter_categories_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]