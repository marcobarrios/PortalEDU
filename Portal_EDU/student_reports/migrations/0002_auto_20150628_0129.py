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
            name='id_student_report',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
