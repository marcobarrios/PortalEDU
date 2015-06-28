# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0001_initial'),
        ('extra_curricular_activity_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCurricularActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_activity', models.CharField(max_length=45)),
                ('date_time_activity', models.CharField(max_length=45)),
                ('duration_extra_curricular_activity', models.PositiveIntegerField(null=True, blank=True)),
                ('description_activity', models.TextField(blank=True)),
                ('include_parents', models.BooleanField(default=0)),
                ('include_students', models.BooleanField(default=1)),
                ('done_activity', models.BooleanField(default=0)),
                ('enable_extra_curricular_activity', models.BooleanField(default=1)),
                ('extra_curricular_activity_type', models.ForeignKey(to='extra_curricular_activity_types.ExtraCurricularActivityType')),
                ('staff', models.ForeignKey(to='staffs.Staff')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
