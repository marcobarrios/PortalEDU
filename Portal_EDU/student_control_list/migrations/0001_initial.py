# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentControlList',
            fields=[
                ('id_student_control_list', models.BigIntegerField(serialize=False, primary_key=True)),
                ('year', models.PositiveIntegerField(blank=True)),
                ('gpa', models.DecimalField(max_digits=5, decimal_places=2, blank=True)),
                ('approved', models.BooleanField(default=0)),
                ('enable_student_control_list', models.BooleanField(default=1)),
                ('grade', models.ForeignKey(to='grades.Grade')),
                ('student', models.ForeignKey(to='students.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
