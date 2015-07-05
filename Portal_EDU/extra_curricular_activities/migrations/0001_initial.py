# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
        ('staffs', '0001_initial'),
        ('extra_curricular_activity_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCurricularActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_activity', models.CharField(max_length=45)),
                ('date_activity', models.DateField()),
                ('time_activity', models.TimeField()),
                ('duration_extra_curricular_activity', models.PositiveIntegerField(help_text=b'En minutos', null=True, blank=True)),
                ('description_activity', models.TextField(blank=True)),
                ('include_parents', models.BooleanField(default=False)),
                ('include_students', models.BooleanField(default=True)),
                ('done_activity', models.BooleanField(default=False)),
                ('enable_extra_curricular_activity', models.BooleanField(default=1)),
                ('extra_curricular_activity_type', models.ForeignKey(to='extra_curricular_activity_types.ExtraCurricularActivityType')),
                ('grade', models.ManyToManyField(to='grades.Grade')),
                ('staff', models.ForeignKey(blank=True, to='staffs.Staff', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
