# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic_calendars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academiccalendar',
            name='grade',
        ),
    ]
