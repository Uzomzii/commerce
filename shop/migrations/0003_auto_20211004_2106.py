# Generated by Django 3.2.7 on 2021-10-04 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='shu',
        ),
    ]
