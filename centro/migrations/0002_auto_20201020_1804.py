# Generated by Django 2.2.5 on 2020-10-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='inventario_contable',
            field=models.BooleanField(default=False),
        ),
    ]