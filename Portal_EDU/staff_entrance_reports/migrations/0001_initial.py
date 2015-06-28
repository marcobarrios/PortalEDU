# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffEntranceReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time_staff_entrance', models.DateTimeField()),
                ('date_time_staff_exit', models.DateTimeField(null=True, blank=True)),
                ('enable_staff_entrance_report', models.BooleanField(default=1)),
                ('staff', models.ForeignKey(to='staffs.Staff')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
