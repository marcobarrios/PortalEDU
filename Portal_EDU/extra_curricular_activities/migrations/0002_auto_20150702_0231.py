# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra_curricular_activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracurricularactivity',
            name='date_time_activity',
            field=models.DateTimeField(max_length=45),
        ),
        migrations.AlterField(
            model_name='extracurricularactivity',
            name='duration_extra_curricular_activity',
            field=models.PositiveIntegerField(help_text=b'En minutos', null=True, blank=True),
        ),
    ]
