# Generated by Django 4.1.3 on 2023-09-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0041_alter_customerlogup_password_reset_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlogup',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
