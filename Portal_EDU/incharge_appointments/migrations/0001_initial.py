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
            name='InchargeAppointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_incharge_appointment', models.CharField(max_length=45, blank=True)),
                ('description_incharge_appointment', models.TextField(blank=True)),
                ('date_time_incharge_appointment', models.DateTimeField(null=True, blank=True)),
                ('duration_incharge_appointment', models.PositiveIntegerField(null=True, blank=True)),
                ('confirmation_incharge_appointment', models.BooleanField(default=0)),
                ('status_incharge_appointment', models.BooleanField(default=1)),
                ('enable_incharge_appointment', models.BooleanField(default=1)),
                ('staff', models.ForeignKey(to='staffs.Staff')),
                ('student', models.ForeignKey(to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
