# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_meeting_schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmeetingschedule',
            name='id_staff_meeting_schedule',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
