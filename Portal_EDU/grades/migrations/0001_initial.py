# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade_names', '0001_initial'),
        ('sections', '0001_initial'),
        ('levels', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_grade_capacity', models.PositiveIntegerField(null=True, blank=True)),
                ('quantity_student_grade', models.PositiveIntegerField(null=True, blank=True)),
                ('enable_grade', models.BooleanField(default=1)),
                ('grade_name', models.ForeignKey(to='grade_names.GradeName')),
                ('level', models.ForeignKey(to='levels.Level')),
                ('section', models.ForeignKey(to='sections.Section')),
                ('staff', models.ForeignKey(blank=True, to='staffs.Staff', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
