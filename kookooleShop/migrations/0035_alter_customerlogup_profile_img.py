# Generated by Django 4.1.3 on 2023-08-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0034_alter_customerlogup_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlogup',
            name='profile_img',
            field=models.ImageField(blank=True, default='/static/image/home-img-3.png', upload_to=''),
        ),
    ]
