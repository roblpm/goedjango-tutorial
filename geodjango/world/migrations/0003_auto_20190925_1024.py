# Generated by Django 2.2.5 on 2019-09-25 10:24

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_auto_20190925_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedingareas',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
    ]