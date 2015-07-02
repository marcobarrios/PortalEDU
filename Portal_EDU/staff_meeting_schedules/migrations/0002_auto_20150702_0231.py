# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_meeting_schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmeetingschedule',
            name='day',
            field=models.CharField(default=b'Lunes', max_length=15, choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'), (b'Mi\xc3\xa9rcoles', b'Mi\xc3\xa9rcoles'), (b'Jueves', b'Jueves'), (b'Viernes', b'Viernes'), (b'S\xc3\xa1bado', b'S\xc3\xa1bado'), (b'Domingo', b'Domingo')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staffmeetingschedule',
            name='date_time_end_staff_meeting_schedule',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='staffmeetingschedule',
            name='date_time_init_staff_meeting_schedule',
            field=models.TimeField(),
        ),
    ]
