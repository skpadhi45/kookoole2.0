# Generated by Django 4.1.3 on 2023-08-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0018_remove_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]