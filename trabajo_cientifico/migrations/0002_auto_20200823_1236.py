# Generated by Django 2.2.5 on 2020-08-23 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0001_initial'),
        ('trabajo_cientifico', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='autores',
        ),
        migrations.AddField(
            model_name='articulo',
            name='autores',
            field=models.ManyToManyField(to='human_resource.Persona'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='referencia_web',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='libro',
            name='autores',
        ),
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.ManyToManyField(to='human_resource.Persona'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='jefe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='human_resource.Persona'),
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='autores',
        ),
        migrations.AddField(
            model_name='resultado',
            name='autores',
            field=models.ManyToManyField(to='human_resource.Persona'),
        ),
    ]