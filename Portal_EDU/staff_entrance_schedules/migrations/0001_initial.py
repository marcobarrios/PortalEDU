# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrance_schedules', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffEntranceSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_staff_entrance_schedule', models.BooleanField(default=True)),
                ('entrance_schedule', models.ManyToManyField(to='entrance_schedules.EntranceSchedule')),
                ('staff', models.ForeignKey(to='staffs.Staff')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
