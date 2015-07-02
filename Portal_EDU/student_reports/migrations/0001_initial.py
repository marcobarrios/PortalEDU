# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_student_report', models.CharField(max_length=45)),
                ('description_student_report', models.TextField(blank=True)),
                ('date_time_sent_report', models.DateTimeField(auto_now_add=True)),
                ('checked_report', models.BooleanField(default=False)),
                ('date_time_checked_report', models.DateTimeField(null=True, blank=True)),
                ('enable_student_report', models.BooleanField(default=1)),
                ('student', models.ForeignKey(to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
