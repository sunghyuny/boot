# Generated by Django 4.2.5 on 2023-10-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]