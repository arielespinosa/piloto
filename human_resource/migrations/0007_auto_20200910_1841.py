# Generated by Django 2.2.16 on 2020-09-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docencia', '0002_auto_20200910_1836'),
        ('trabajo_cientifico', '0003_auto_20200910_1836'),
        ('human_resource', '0006_auto_20200910_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='certificaciones',
            field=models.ManyToManyField(to='docencia.Certificacion'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='eventos',
            field=models.ManyToManyField(to='docencia.Evento'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='literatura_gris',
            field=models.ManyToManyField(to='trabajo_cientifico.LiteraturaGris'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='oponencias',
            field=models.ManyToManyField(to='docencia.Oponencia'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='resultados',
            field=models.ManyToManyField(to='trabajo_cientifico.Resultado'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='tesis',
            field=models.ManyToManyField(to='docencia.Tesis'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='tribunales',
            field=models.ManyToManyField(to='docencia.Tribunal'),
        ),
    ]
