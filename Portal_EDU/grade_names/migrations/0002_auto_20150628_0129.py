# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade_names', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradename',
            name='id_grade_name',
            field=models.BigIntegerField(serialize=False, editable=False, primary_key=True),
        ),
    ]
