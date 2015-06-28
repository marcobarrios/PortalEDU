# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade_names', '0001_initial'),
        ('sections', '0001_initial'),
        ('levels', '0001_initial'),
        ('extra_curricular_activities', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_grade', models.BooleanField(default=1)),
                ('extra_curricular_activities', models.ManyToManyField(to='extra_curricular_activities.ExtraCurricularActivity')),
                ('grade_name', models.ForeignKey(to='grade_names.GradeName')),
                ('level', models.ForeignKey(to='levels.Level')),
                ('section', models.ForeignKey(to='sections.Section')),
                ('staff', models.ForeignKey(to='staffs.Staff')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
