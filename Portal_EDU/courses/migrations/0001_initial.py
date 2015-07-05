# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('schedules', '0001_initial'),
        ('classrooms', '0001_initial'),
        ('modules', '0001_initial'),
        ('grades', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_student_capacity_course', models.PositiveIntegerField(null=True, blank=True)),
                ('quantity_student_course', models.PositiveIntegerField(null=True, blank=True)),
                ('enable_course', models.BooleanField(default=1)),
                ('classroom', models.ForeignKey(blank=True, to='classrooms.ClassRoom', null=True)),
                ('grade', models.ForeignKey(to='grades.Grade')),
                ('module', models.ForeignKey(to='modules.Module')),
                ('schedule', models.ManyToManyField(to='schedules.Schedule', null=True, blank=True)),
                ('staff', models.ForeignKey(blank=True, to='staffs.Staff', null=True)),
                ('subject', models.ForeignKey(to='subjects.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
