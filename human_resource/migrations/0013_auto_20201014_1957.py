# Generated by Django 2.2.5 on 2020-10-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0012_auto_20201014_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='foto',
            field=models.ImageField(default='avatar_default.jpg', null=True, upload_to='fotos_de_perfiles'),
        ),
    ]
