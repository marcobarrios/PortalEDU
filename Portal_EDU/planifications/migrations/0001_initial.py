# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planification_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planification',
            fields=[
                ('id_planification', models.BigIntegerField(serialize=False, primary_key=True)),
                ('planification_file', models.FileField(upload_to=b'planifitacion_files/%Y/%m/%d/', blank=True)),
                ('description_planification', models.TextField(null=True, blank=True)),
                ('enable_planification', models.BooleanField(default=1)),
                ('planifitacion_type', models.ForeignKey(to='planification_types.PlanificationType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
