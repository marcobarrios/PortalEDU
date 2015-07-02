# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_entrance_reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffentrancereport',
            name='date_time_staff_entrance',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='staffentrancereport',
            name='date_time_staff_exit',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
