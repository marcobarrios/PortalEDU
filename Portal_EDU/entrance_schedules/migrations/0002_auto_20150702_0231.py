# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrance_schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entranceschedule',
            name='entrance_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='entranceschedule',
            name='leave_time',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
