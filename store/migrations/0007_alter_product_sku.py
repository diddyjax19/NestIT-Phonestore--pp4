# Generated by Django 3.2.3 on 2023-09-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20230613_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=155, null=True, unique=True, verbose_name='Unique Product\xa0ID\xa0(SKU)'),
        ),
    ]
