# Generated by Django 2.2.5 on 2020-10-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0010_auto_20201013_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='areas_de_interes',
            field=models.ManyToManyField(blank=True, null=True, to='human_resource.AreasInteres'),
        ),
    ]