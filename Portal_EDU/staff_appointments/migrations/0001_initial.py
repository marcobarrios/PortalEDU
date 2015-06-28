# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAppointment',
            fields=[
                ('id_staff_appointment', models.BigIntegerField(serialize=False, primary_key=True)),
                ('subject_staff_appointment', models.CharField(max_length=45, blank=True)),
                ('description_staff_appointment', models.CharField(max_length=45, blank=True)),
                ('date_time_staff_appointment', models.DateTimeField(null=True, blank=True)),
                ('duration_staff_appointment', models.PositiveIntegerField(null=True, blank=True)),
                ('confirmation_staff_appointment', models.BooleanField(default=0)),
                ('status_staff_appointment', models.BooleanField(default=1)),
                ('enable_staff_appointment', models.BooleanField(default=1)),
                ('staff', models.ForeignKey(to='staffs.Staff')),
                ('student', models.ForeignKey(to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
