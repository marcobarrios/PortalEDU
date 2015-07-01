# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planification_types', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_planification', models.CharField(max_length=45)),
                ('description_planification', models.TextField(null=True, blank=True)),
                ('planification_file', models.FileField(upload_to=b'planifitacion_files/%Y/%m/%d/', blank=True)),
                ('enable_planification', models.BooleanField(default=1)),
                ('course', models.ForeignKey(to='courses.Course')),
                ('planifitacion_type', models.ForeignKey(to='planification_types.PlanificationType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
