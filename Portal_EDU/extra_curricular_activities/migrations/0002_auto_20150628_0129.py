# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra_curricular_activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extracurricularactivity',
            name='id_extra_curricular_activity',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
