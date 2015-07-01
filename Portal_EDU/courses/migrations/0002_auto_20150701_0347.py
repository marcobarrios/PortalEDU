# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='planification',
        ),
        migrations.AlterField(
            model_name='course',
            name='classroom',
            field=models.ForeignKey(blank=True, to='classrooms.ClassRoom', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='schedule',
            field=models.ForeignKey(blank=True, to='schedules.Schedule', null=True),
        ),
    ]
