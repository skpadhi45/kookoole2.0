# Generated by Django 4.1.3 on 2023-02-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0007_alter_customerlogup_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlogup',
            name='pin',
            field=models.CharField(default='', max_length=10),
        ),
    ]
