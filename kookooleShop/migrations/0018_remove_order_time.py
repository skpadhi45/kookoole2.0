# Generated by Django 4.1.3 on 2023-08-06 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0017_order_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='time',
        ),
    ]