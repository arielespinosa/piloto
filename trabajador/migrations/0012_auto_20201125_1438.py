# Generated by Django 2.2.5 on 2020-11-25 19:38

import datetime
from django.db import migrations, models
import gm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('trabajador', '0011_auto_20201125_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesis',
            name='tutores',
            field=gm2m.fields.GM2MField('trabajador.Trabajador', 'trabajador.PersonaExterna', related_name='tesis_tutoradas', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk')),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2020, 11, 25, 14, 38, 30, 324159)),
        ),
    ]