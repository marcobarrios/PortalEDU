# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True)),
                ('ponderation', models.DecimalField(default=0.0, max_digits=4, decimal_places=2)),
                ('delivery_date', models.DateTimeField(null=True, blank=True)),
                ('need_file', models.BooleanField(default=False)),
                ('enable_academic_calendar', models.BooleanField(default=1)),
                ('assignment', models.ForeignKey(to='assignments.Assignment')),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
