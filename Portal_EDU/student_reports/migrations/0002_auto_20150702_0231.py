# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreport',
            name='date_time_sent_report',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='studentreport',
            name='subject_student_report',
            field=models.CharField(max_length=45),
        ),
    ]
