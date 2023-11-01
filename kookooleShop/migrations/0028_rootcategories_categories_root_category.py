# Generated by Django 4.1.3 on 2023-08-17 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kookooleShop', '0027_customerlogup_token_customerlogup_verify'),
    ]

    operations = [
        migrations.CreateModel(
            name='RootCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='root_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kookooleShop.rootcategories'),
        ),
    ]
