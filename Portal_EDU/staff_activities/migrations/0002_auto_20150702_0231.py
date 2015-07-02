# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff_activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffactivity',
            name='descripcion_staff_activity',
            field=models.TextField(blank=True),
        ),
    ]
