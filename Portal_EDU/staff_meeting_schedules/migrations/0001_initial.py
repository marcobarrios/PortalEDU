# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffMeetingSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time_init_staff_meeting_schedule', models.DateTimeField()),
                ('date_time_end_staff_meeting_schedule', models.DateTimeField()),
                ('enable_staff_meeting_schedule', models.BooleanField(default=1)),
                ('staff', models.ForeignKey(to='staffs.Staff')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
