# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic_calendars', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivered_date_task', models.DateTimeField(auto_now=True)),
                ('checked_task', models.BooleanField(default=0)),
                ('file_task', models.FileField(upload_to=b'task_files/%Y/%m/%d/', blank=True)),
                ('teacher_commentary_task', models.TextField(blank=True)),
                ('enable_task', models.BooleanField(default=1)),
                ('academic_calendar', models.ForeignKey(to='academic_calendars.AcademicCalendar')),
                ('student', models.ForeignKey(to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
